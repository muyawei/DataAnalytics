# coding: utf-8
import pandas as pd
from datetime import datetime, timedelta, date
from contextlib import closing
from sqlalchemy import func,distinct
from sqlalchemy.orm import aliased

from v8.model.martin import UserRegister, UserAndroid, UserIphone
from v8.model.base import City
from v8.model.order import OrderOilFull
from v8.engine.db_conn import gen_session_class, gen_mongo_connection
from v8.config import config, config_ucloud

from receipts_config import test
from util import put_file, \
    get_oil_station_city_name, mail, add_attachment, \
    get_test

from config import sentry_uri
from decorators import singleton, sentry
from db_conn import get_hive_class_cron
from model import HiveUser
config.from_object(config_ucloud)
base_slave = gen_session_class('base_slave')
order_slave = gen_session_class('martin_order_slave')
hive_session = get_hive_class_cron('base')()


def datetime_format(date_time):
    return date_time.replace(
        hour=0, minute=0, second=0, microsecond=0)


def get_order_oils_full(start_time, end_time):
    user_ids = []
    filters = [OrderOilFull.paid == 1,
               OrderOilFull.create_time >= start_time,
               OrderOilFull.create_time < end_time,
               ~OrderOilFull.summary.like(u'%%设备%%'),
               ~OrderOilFull.summary.like(u'%%测试%%'),
               ~OrderOilFull.summary.like(u'%%商务%%'),
               ~OrderOilFull.summary.like(u'%%微车%%')]
    query_keys = ['_id']
    queries = [OrderOilFull.user_id.label('_id')]
    with closing(order_slave()) as session:
        for _order in session.query(*queries) \
                .filter(*filters):
            for k in query_keys:
                value = getattr(_order, k)
            user_ids.append(value)
        return user_ids


def get_order_oils_device_id(user_ids):
    id_list = list()
    for i in user_ids:
        id_list.append(int(i))
    device_ids = []
    with closing(base_slave()) as session:
        for device_id, in session.query(UserRegister.device_id) \
                .filter(UserRegister.id.in_(id_list)):
            device_ids.append(device_id)
        return device_ids


def get_order_oils_channel(device_ids):
    device_id_channel = {}
    device_id_city = {}
    with closing(base_slave()) as session:
        for device_id, _channel, city in session.query(
                           UserAndroid.id,
                           UserAndroid.channel,
                           UserAndroid.city).filter(
                           UserAndroid.id.in_(device_ids)):
            if device_id:
                device_id_channel[device_id] = _channel
                device_id_city[device_id] = city

        for device_id, _channel, city in session.query(
                          UserIphone.id,
                          UserIphone.channel,
                          UserIphone.city) \
                .filter(UserIphone.id.in_(device_ids)):
            if device_id:
                device_id_channel[device_id] = _channel
                device_id_city[device_id] = city
        return device_id_channel, device_id_city


def get_city_to_province():
    city_to_province = {}
    with closing(base_slave()) as session:
        for city, province in session.query(City.city_name,
                                            City.province_name):
            city_to_province[city] = province
        return city_to_province


def get_count_oil_by_province_channel(device_id_channel, device_id_city,
                                      city_to_province):
    channel_province = dict()
    for key in device_id_channel:
        channel = device_id_channel[key]
        city = device_id_city[key]
        if city:
            province = city_to_province[city]
        else:
            provice = ""
        channel_province.setdefault(province, {}).setdefault(channel, 0)
        channel_province[province][channel] += 1
    return channel_province


def get_accum_register_by_hive(end_time):
    with closing(hive_session) as session:
        user_register = aliased(HiveUser)
        user_andr_phone = aliased(HiveUser)
        accum_register = []
        for sum, channel in session.query(
                    func.count(distinct(user_register.id)).label("sum"),
                    user_andr_phone.channel).filter(
                    user_register.platform == "register",
                    user_andr_phone.platform.in_(["android", "iphone"]),
                    user_register.device_id == user_andr_phone.id,
                    user_register.create_date < end_time ).group_by(
                    user_andr_phone.channel):
            register_info = {}
            register_info[u"累计注册"] = sum
            register_info["_channel"] = channel
            accum_register.append(register_info)
        return accum_register


def get_register_device_id(start_time, end_time):
    device_ids = []
    device_ids_weixin = []
    device_ids_phone = []
    with closing(base_slave()) as session:
        for device_id, weixin, phone in session.query(
                UserRegister.device_id, UserRegister.weixin_openid,
                UserRegister.phone).filter(
                UserRegister.create_time >= start_time,
                UserRegister.create_time < end_time):
            device_ids.append(device_id)
            if weixin:
                device_ids_weixin.append(device_id)
            if phone:
                device_ids_phone.append(device_id)
        return device_ids, device_ids_weixin, device_ids_phone


def get_register_by_channel(device_ids):
    device_id_channel = {}
    with closing(base_slave()) as session:
        for device_id, _channel in session.query(
                UserAndroid.id, UserAndroid.channel).filter(
                UserAndroid.id.in_(device_ids)):
            if device_ids:
                device_id_channel[device_id] = _channel

        for device_id, _channel in session.query(
                UserIphone.id, UserIphone.channel) .filter(
                UserIphone.id.in_(device_ids)):
            if device_ids:
                device_id_channel[device_id] = _channel

        return device_id_channel


def get_count_register(device_id_channel):
    channel = dict()
    for key in device_id_channel:
        _channel = device_id_channel[key]
        channel.setdefault(_channel, 0)
        channel[_channel] += 1
    return channel


def save_file(start_time, end_time, file_name):
    writer = pd.ExcelWriter(file_name)
    start = start_time
    end = end_time
    sheet_oil = str(start) + u"加油统计"
    sheet_regis = str(start) + u"注册数据"
    user_ids = get_order_oils_full(start, end)
    device_ids = get_order_oils_device_id(user_ids)
    device_id_channel, device_id_city = get_order_oils_channel(device_ids)
    city_to_province = get_city_to_province()
    channel_province = get_count_oil_by_province_channel(
        device_id_channel, device_id_city,
        city_to_province)
    df_oil = pd.DataFrame(channel_province)
    df_oil = df_oil.fillna(value=0)
    df_oil[u"总订单"] = df_oil.sum(axis=1)
    df_oil.index.name = u"渠道"
    device_ids, device_ids_weixin, device_ids_phone = get_register_device_id(
        start_time, end_time)
    register_day = get_count_register(
        get_register_by_channel(device_ids))
    register_weixin = get_count_register(
        get_register_by_channel(device_ids_weixin))
    register_phone = get_count_register(
        get_register_by_channel(device_ids_phone))
    register_accum = get_accum_register_by_hive(end_time)
    df_day = pd.Series(register_day)
    df_weixin = pd.Series(register_weixin)
    df_phone = pd.Series(register_phone)
    df_accum = pd.DataFrame(register_accum)
    df = pd.concat([df_day, df_weixin, df_phone], axis=1)
    df = df.fillna(value=0)
    df = pd.DataFrame(df.values, columns=[u"总注册", u"微信注册", u"手机注册"],
                      index=df.index)
    d = pd.merge(df, df_accum, left_index=True, right_on="_channel",
                 how="outer")
    day_weixin_phone_accum = d.reindex(
        columns=["_channel", u"总注册", u"微信注册", u"手机注册", u"累计注册"])
    df_oil.to_excel(writer, sheet_name=sheet_oil)
    day_weixin_phone_accum.to_excel(writer, sheet_name=sheet_regis)
    writer.close()


def send_mail(start_time, end_time):
    import uuid
    email = dict()
    email['subject'] = u'{start_date}-{end_date}加油统计与注册数据'.format(
        start_date=start_time,
        end_date=end_time)
    file_name = u'{uuid}{start_date}-{end_date}加油统计与注册数据.xlsx'.format(
        start_date=start_time,
        end_date=end_time,
        uuid=uuid.uuid4().hex)
    receipts = get_test(test)
    email['to'] = ','.join(receipts)
    subject = u'加油订单与注册数据详情, 点击下载'
    save_file(start_time, end_time, file_name)
    with open(file_name, 'rb') as of:
        attachment_url = put_file(file_name, of)
        email['html'] = u'<a href=%s>%s</a>' % (attachment_url, subject)
    mail(email)

if __name__ == "__main__":
        start_time = date(2016, 11, 1)
        end_time = date(2016, 11, 2)
        send_mail(start_time, end_time)
