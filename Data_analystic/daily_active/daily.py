# -*- coding: utf-8 -*-
# coding: utf-8
from contextlib import closing
from datetime import datetime, timedelta

import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import func, distinct

from config import V8_CONFIG
from v8.config import config
from v8.engine.db_conn import gen_session_class
from v8.model.martin import UserAndroid, UserIphone
from v8.model.base import City

from config import sentry_uri
from decorators import sentry, singleton
from db_conn import gen_session_class_cron
from model import ActiveUseCityDay, Event, EventCountPv, EventCountUv
from receipts_config import daily_active_and_app_count_receipts, test
from util import get_test, mail, put_file, render

config.from_object(V8_CONFIG)
base_session = gen_session_class('base_slave')
spark_session = gen_session_class_cron('spark')
sky_session = gen_session_class_cron('sky')


def query_daily_active_cnt(one_time, month_time):
    with closing(spark_session()) as session:
        data_sum = list()
        for daily_active_cnt in session.query(
            func.sum(ActiveUseCityDay.count)).filter(
            ActiveUseCityDay.date.between(one_time, month_time), ActiveUseCityDay.app_name.notlike('%_weiche'))\
                .group_by(ActiveUseCityDay.date):
            data_sum.append(daily_active_cnt)
        return data_sum


def query_daily_city(one_time):
    with closing(spark_session()) as session:
        daily_active = session.query(
            ActiveUseCityDay.city, func.sum(ActiveUseCityDay.count).label('sum')).filter(
            ActiveUseCityDay.date == one_time,
            ActiveUseCityDay.app_name.notlike('%_weiche')).group_by(ActiveUseCityDay.city)
        return daily_active


def query_daily_province(city_datas):
    province_sum = dict()
    with closing(base_session()) as session:
        for city_data in city_datas:
            for city in session.query(City).filter(City.city_name == city_data.city):
                    province_sum.setdefault(city.province_name, 0)
                    province_sum[city.province_name] += city_data.sum
        print province_sum
        return province_sum


def query_active_by_app(one_time, month_time, app_name):
    with closing(spark_session()) as session:
        data_app = list()
        for daily_ios_cnt in session.query(
            func.sum(ActiveUseCityDay.count)).filter(
            ActiveUseCityDay.date.between(one_time, month_time), ActiveUseCityDay.app_name == app_name)\
                .group_by(ActiveUseCityDay.date):
            data_app.append(daily_ios_cnt)
        return data_app


def query_max_user(model, one_time):
    with closing(base_session()) as session:
        user = session.query(model).filter(model.create_time < one_time) \
            .order_by(model.id.desc()).first()
        return user


def query_new_user(yesterday_id, today_id, model):
    with closing(base_session()) as session:
        cnt = session.query(
            func.count(distinct(func.concat(model.imei, model.imsi)))).filter(
            model.id.between(yesterday_id, today_id), model.app_name.notlike('%_weiche')).scalar()
        return cnt


def query_sum_new_user(today_time, yesterday_time):
        iphone_min_id = query_max_user(UserIphone, yesterday_time).id + 1
        iphone_max_id = query_max_user(UserIphone, today_time).id
        new_iphone_cnt = query_new_user(iphone_min_id, iphone_max_id, UserIphone)

        android_min_id = query_max_user(UserAndroid, yesterday_time).id + 1
        android_max_id = query_max_user(UserAndroid, today_time).id
        new_android_cnt = query_new_user(android_min_id, android_max_id, UserAndroid)

        return new_iphone_cnt + new_android_cnt


def app_count(one_time, event_id, event_name, app_name):
    with closing(sky_session()) as session:
        events = dict()
        for event, app_cnt in session.query(
                Event, func.sum(event_name.count)).filter(
                Event.id == event_name.event_id).group_by(
                event_name.event_id).filter(
                    event_name.date == one_time).filter(event_name.app_name == app_name).filter(
                "event_id=:id").params(id=event_id):
                events['id'] = event.id
                events['name'] = event.name
                events['sum'] = app_cnt
        return events


def get_app_data(yesterday_time, event_name, app_name, app_events):
    apps = list()
    for i in range(0, len(app_events)):
        app = app_count(yesterday_time, app_events[i], event_name, app_name)
        if app:
            apps.append(app)
    return apps


def get_dailys_data(activate_time, act_time, today_time, yesterday_time):
    dailys = dict()
    daily_active_cnt = query_daily_active_cnt(activate_time, act_time)[0]
    daily_android_cnt = query_active_by_app(activate_time, act_time, 'cn.buding.martin')[0]
    daily_ios_cnt = query_active_by_app(activate_time, act_time, 'AstonMartin')[0]
    small_active_cnt = daily_active_cnt - daily_android_cnt - daily_ios_cnt
    new_user_cnt = query_sum_new_user(today_time, yesterday_time)
    user_rate = "%.3f" % (new_user_cnt / daily_active_cnt)
    dailys['daily_active_cnt'] = daily_active_cnt
    dailys['new_user_cnt'] = new_user_cnt
    dailys['user_rate'] = user_rate
    dailys['daily_android_cnt'] = daily_android_cnt
    dailys['daily_ios_cnt'] = daily_ios_cnt
    dailys['small_active_cnt'] = small_active_cnt
    return dailys


def get_month_analytics(activate_time, month_time):
    cnt_sum = query_daily_active_cnt(activate_time, month_time)
    cnt_and = query_active_by_app(activate_time, month_time, 'cn.buding.martin')
    cnt_ios = query_active_by_app(activate_time, month_time, 'AstonMartin')
    print cnt_sum
    print cnt_and
    print cnt_ios
    df = pd.DataFrame([cnt_sum, cnt_and, cnt_ios], index=['sum', 'and', 'ios'])
    df_reve = df.T
    data_sum_and = df_reve['and'].values
    data_sum_ios = df_reve['ios'].values
    data_sum = df_reve['sum'].values
    data_sum_small = data_sum - data_sum_and - data_sum_ios

    x_index = range(1, 16)
    date = list()
    for i in range(15, 0, -1):
        date.append((datetime.now() - timedelta(days=i)).strftime("%m-%d"))

    print date

    plt.xticks(x_index, date)

    plt.bar(x_index, data_sum_and, width=0.1, align="center", color='g', label="android")
    plt.bar(x_index, data_sum_ios, bottom=data_sum_and, width=0.1, align="center", color='b', label='ios')
    plt.bar(x_index, data_sum_small, bottom=data_sum_ios + data_sum_and, width=0.1, align="center", color='y',
            label=u"小版本")
    plt.plot(x_index, data_sum, color='r', label="sum")
    plt.legend(loc='best')
    plt.title(u"日活走势站内")
    plt.show()


@sentry(sentry_uri)
@singleton('/tmp/daily_active.pid')
def send_mail():
    activate_time = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")
    yes_time = (datetime.now() - timedelta(days=1)).strftime("%m-%d")
    month_time = (datetime.now() - timedelta(days=15)).strftime("%m-%d")
    today_time = datetime.now().strftime("%Y-%m-%d")
    yesterday_time = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    app_events_one = [1350, 1349, 1559, 1558, 1557, 1556, 1555, 1554, 1553, 1531, 1530, 1529, 1528, 1527, 1526, 1525,
                      1524, 1523, 1374, 1351, 1560, 1552, 1551, 1094]
    app_events_two = [1129, 1133, 1134, 1539, 1138, 1132, 1130, 1540, 1541, 1542, 1543, 1166, 1131, 1143, 1141, 1140,
                      1142, 1545, 1146, 1145, 1148, 1147, 1260, 1149, 1150, 1546, 1160, 1534, 1532, 1533, 1546, 1160,
                      1547, 1162, 1548, 1332, 1535, 1538, 1164, 1256, 1258, 1139, 1144, 1163, 1159, 1161, 1550]
    dailys = get_dailys_data(activate_time, activate_time, today_time, yesterday_time)
    get_month_analytics(month_time, yes_time)
    province_sum = query_daily_province(query_daily_city(activate_time))
    pv_ios = get_app_data(yesterday_time, EventCountPv, "AstonMartin", app_events_one)
    pv_and = get_app_data(yesterday_time, EventCountPv, "cn.buding.martin", app_events_one)
    uv_ios = get_app_data(yesterday_time, EventCountUv, "AstonMartin", app_events_one)
    uv_and = get_app_data(yesterday_time, EventCountUv, "cn.buding.martin", app_events_one)
    pv_ios_two = get_app_data(yesterday_time, EventCountPv, "AstonMartin", app_events_two)
    pv_and_two = get_app_data(yesterday_time, EventCountPv, "cn.buding.martin", app_events_two)
    uv_ios_two = get_app_data(yesterday_time, EventCountUv, "AstonMartin", app_events_two)
    uv_and_two = get_app_data(yesterday_time, EventCountUv, "cn.buding.martin", app_events_two)
    send_date = (datetime.now() - timedelta(days=1)).strftime("%m-%d")
    print uv_and
    html = render('daily_active.html',
                  dailys=dailys,
                  province_sum=province_sum,
                  uv_ios=uv_ios,
                  uv_and=uv_and,
                  pv_ios=pv_ios,
                  pv_and=pv_and,
                  pv_ios_two=pv_ios_two,
                  pv_and_two=pv_and_two,
                  uv_ios_two=uv_ios_two,
                  uv_and_two=uv_and_two,
                  send_date=send_date)
    email = {
        'subject': u'站内日活及app点位数据统计 %s' % activate_time,
        'to': ','.join(get_test(test)),
        'html': html.encode('utf-8')}
    mail(email)


if __name__ == '__main__':
    send_mail()
