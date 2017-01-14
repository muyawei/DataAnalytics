#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
from contextlib import closing

from config import V8_CONFIG
from v8.config import config
from xlwt import Workbook

config.from_object(V8_CONFIG)

from v8.engine.db_conn import gen_session_class
from v8.engine.util import model_to_dict
from v8.model.martin import OrderBase, OrderViolationPayment, UserRegister, \
    UserIphone, UserAndroid

import util
from model import ViolationPaymentOrderChannelStat
from decorators import singleton, sentry
from config import sentry_uri
from script.analytics.oil_order_and_register_analytics import \
    get_attachment_url
# receipts = 'chenyigang@weiche.cn'
receipts = ','.join(['chenyigang@weiche.cn',
                     'yushenghui@weiche.cn',
                     'shizekui@weiche.cn'])


def get_device_ids(user_ids):
    user_id_device_id = dict()
    with closing(gen_session_class('base_slave')()) as session:
        for user_id, device_id in session.query(
                UserRegister.id, UserRegister.device_id
        ).filter(
            UserRegister.id.in_(user_ids)
        ):
            user_id_device_id[user_id] = device_id
    return user_id_device_id


def get_iphone_channel(device_ids):
    device_id_channel = dict()
    with closing(gen_session_class('base_slave')()) as session:
        for device_id, channel in session.query(
                UserIphone.id, UserIphone.channel
        ).filter(
            UserIphone.id.in_(device_ids)
        ):
            device_id_channel[device_id] = channel
    return device_id_channel


def get_android_channel(device_ids):
    device_id_channel = dict()
    with closing(gen_session_class('base_slave')()) as session:
        for device_id, channel in session.query(
                UserAndroid.id, UserAndroid.channel
        ).filter(
            UserAndroid.id.in_(device_ids)
        ):
            device_id_channel[device_id] = channel
    return device_id_channel


def count_order_user_channel_daily(day):
    """count the order of user's channel per day and send email"""

    start_time = day
    end_time = day + datetime.timedelta(days=1)

    with closing(gen_session_class('martin_order_slave')()) as session:
        user_ids = []
        abr_order = dict()
        for order, vio_pay in session.query(
                OrderBase, OrderViolationPayment
        ).filter(
                    OrderBase.id == OrderViolationPayment.order_id
        ).filter(
                    OrderBase.order_type == 'violation_payment',
                    OrderBase.create_time >= start_time,
                    OrderBase.create_time < end_time,
                    OrderBase.paid > 0):
            vehicle_license_plate_num = vio_pay.vehicle_license_plate_num
            partner_id = vio_pay.partner_id
            # filter
            if vehicle_license_plate_num.startswith(u"藏") or partner_id == 3:
                continue
            user_ids.append(order.user_id)
            abr = vehicle_license_plate_num[0:1]
            abr_order.setdefault(abr, []).append(model_to_dict(order))

        user_id_device_id = get_device_ids(user_ids)
        device_ids = set()
        for user_id, device_id in user_id_device_id.iteritems():
            device_ids.add(device_id)
        device_id_channel_android = get_android_channel(device_ids)
        device_id_channel_iphone = get_iphone_channel(device_ids)

        device_id_channel = dict()
        channel_platform = dict()
        for device_id in device_ids:
            if device_id in device_id_channel_android:
                channel = device_id_channel_android[device_id]
                channel_platform[channel] = "android"
                device_id_channel[device_id] = channel
            elif device_id in device_id_channel_iphone:
                channel = device_id_channel_iphone[device_id]
                channel_platform[channel] = "iphone"
                device_id_channel[device_id] = channel

        channel_area = dict()
        area_set = set()
        channel_total = dict()
        user_visited = dict()
        device_visited = dict()

        for abr, orders in abr_order.iteritems():
            area_set.add(abr)
            for order in orders:
                user_id = order['user_id']
                if user_id in user_id_device_id and user_id_device_id[
                    user_id] in device_id_channel:
                    device_id = user_id_device_id[user_id]
                    channel = device_id_channel[device_id]
                    if channel not in channel_area or abr not in channel_area[
                        channel]:
                        channel_area.setdefault(channel, dict()).setdefault(
                            abr, dict()).setdefault('user_count', 0)
                        channel_area.setdefault(channel, dict()).setdefault(
                            abr, dict()).setdefault('order_count', 0)

                        channel_total.setdefault(channel, dict()).setdefault(
                            'order_count', 0)
                        channel_total.setdefault(channel, dict()).setdefault(
                            'user_count', 0)

                        user_visited.setdefault(channel, set())
                        device_visited.setdefault(channel, set())

                    if user_id not in user_visited[channel]:
                        channel_area[channel][abr]['user_count'] += 1
                        channel_area[channel][abr]['order_count'] += 1
                        user_visited[channel].add(user_id)

                        if device_id not in device_visited:
                            device_visited[channel].add(device_id)
                            channel_total[channel]['user_count'] += 1
                    else:
                        channel_area[channel][abr]['order_count'] += 1

                    channel_total[channel]['order_count'] += 1

    return channel_area, channel_total, channel_platform, list(area_set)


def get_year_months(start_date, end_date):
    """
    get all year-month-day
    """
    ret = []
    start_date = start_date.date()
    end_date = end_date + datetime.timedelta(days=1)
    end_date = end_date.date()
    with closing(gen_session_class('martin_order_slave')()) as session:
        stmt = ('select date(create_time) '
                'from order_base  '
                'where paid > 0 and order_type = "violation_payment" '
                'group by date(create_time) '
                'order by date(create_time) ')
        for create_time in session.execute(stmt):
            day = create_time[0]
            if start_date <= day < end_date:
                ret.append(day)
    return ret


def count_order_user_channel_history(start_date, end_date):
    """history record from start_date to end_date"""
    days = get_year_months(start_date, end_date)

    user_book = Workbook('utf-8')
    order_book = Workbook('utf-8')
    for day in days:
        sheet_total_user = user_book.add_sheet(str(day))
        sheet_total_order = order_book.add_sheet(str(day))

        channel_area, channel_total, channel_platform, area_list = \
            count_order_user_channel_daily(day)

        for index, area in enumerate(area_list):
            sheet_total_user.write(0, index + 1, area)
            sheet_total_order.write(0, index + 1, area)
        sheet_total_user.write(0, len(area_list) + 1, u'合计')
        sheet_total_order.write(0, len(area_list) + 1, u'合计')

        total_order_infos = []
        total_user_infos = []
        for chan, areas in channel_area.iteritems():
            order_info = [chan]
            user_info = [chan]
            for area in area_list:
                order_count = 0
                user_count = 0
                if area in areas.keys():
                    order_count = areas[area]['order_count']
                    user_count = areas[area]['user_count']
                order_info.append(order_count)
                user_info.append(user_count)
            order_info.append(channel_total[chan]['order_count'])
            user_info.append(channel_total[chan]['user_count'])

            total_order_infos.append(order_info)
            total_user_infos.append(user_info)

        for i, row in enumerate(total_order_infos):
            for j, col in enumerate(row):
                sheet_total_order.write(i + 1, j, col)

        for i, row in enumerate(total_user_infos):
            for j, col in enumerate(row):
                sheet_total_user.write(i + 1, j, col)

    user_file_name = str(start_date.date()) + '_' + str(
        end_date.date()) + u'_订单渠道用户统计.xls'
    order_file_name = str(start_date.date()) + '_' + str(
        end_date.date()) + u'_订单渠道统计.xls'
    if len(days) != 0:
        user_book.save(user_file_name)
        order_book.save(order_file_name)
    else:
        print 'no result data'


@sentry(sentry_uri)
@singleton('/tmp/count_user_channel_daily_report.pid')
def cron_count_data_daily():
    now = datetime.datetime.now()
    today = datetime.datetime(now.year, now.month, now.day)
    yesterday = today + datetime.timedelta(days=-1)

    channel_area, channel_total, channel_platform, area_list = \
        count_order_user_channel_daily(yesterday)

    # insert into mysql
    with closing(gen_session_class('martin_analytics')()) as session:
        for channel, areas in channel_area.iteritems():
            for area, count in areas.iteritems():
                violation_payment = \
                    ViolationPaymentOrderChannelStat(
                        stat_date=yesterday.date(),
                        channel=channel,
                        license_prefix=area,
                        platform=channel_platform[channel],
                        order_count=count['order_count'],
                        user_count=count['user_count'],
                        create_time=now,
                        update_time=now
                    )
                session.add(violation_payment)
        for channel, cnt in channel_total.iteritems():
            violation_payment = ViolationPaymentOrderChannelStat(
                stat_date=yesterday.date(),
                channel=channel,
                license_prefix='',
                platform=channel_platform[channel],
                order_count=cnt['order_count'],
                user_count=cnt['user_count'],
                create_time=now,
                update_time=now
            )
            session.add(violation_payment)
        session.commit()

    yesterday_total_order = []
    yesterday_total_user = []
    for chan, areas in channel_area.iteritems():
        order_info = [chan]
        user_info = [chan]
        for area in area_list:
            order_count = 0
            user_count = 0
            if area in areas.keys():
                order_count = areas[area]['order_count']
                user_count = areas[area]['user_count']
            order_info.append(order_count)
            user_info.append(user_count)
        order_info.append(channel_total[chan]['order_count'])
        user_info.append(channel_total[chan]['user_count'])

        yesterday_total_order.append(order_info)
        yesterday_total_user.append(user_info)

    # send email
    mail = dict()
    mail['to'] = receipts
    mail['subject'] = str(yesterday.date()) + u' 订单渠道统计'
    mail['html'] = util.render(
        'count_order_user_channel_daily_report.html',
        attachment_url=get_attachment_url(yesterday, today),
        area_list=area_list,
        yesterday_total_order=yesterday_total_order,
        yesterday_total_user=yesterday_total_user,
    )
    util.mail(mail)


def save_history_data(start_date, end_date):
    """save history data to mysql"""
    days = get_year_months(start_date, end_date)
    now = datetime.datetime.now()
    with closing(gen_session_class('martin_analytics')()) as session:
        for day in days:
            channel_area, channel_total, channel_platform, area_list = \
                count_order_user_channel_daily(day)

            for channel, areas in channel_area.iteritems():
                for area, count in areas.iteritems():
                    violation_payment = \
                        ViolationPaymentOrderChannelStat(
                            stat_date=day,
                            channel=channel,
                            license_prefix=area,
                            platform=channel_platform[channel],
                            order_count=count['order_count'],
                            user_count=count['user_count'],
                            create_time=now,
                            update_time=now
                        )
                    session.add(violation_payment)
            for channel, cnt in channel_total.iteritems():
                violation_cccayment = ViolationPaymentOrderChannelStat(
                    stat_date=day,
                    channel=channel,
                    license_prefix='',
                    platform=channel_platform[channel],
                    order_count=cnt['order_count'],
                    user_count=cnt['user_count'],
                    create_time=now,
                    update_time=now
                )
                session.add(violation_payment)
            session.commit()


if __name__ == '__main__':
    # start_date = datetime.datetime.strptime('2016-11-1', '%Y-%m-%d')
    # end_date = datetime.datetime.strptime('2016-12-26', '%Y-%m-%d')
    # count_order_user_channel_history(start_date, end_date)
    # start_date = datetime.datetime.strptime('2014-11-18', '%Y-%m-%d')
    # end_date = datetime.datetime.strptime('2017-1-4', '%Y-%m-%d')
    # save_history_data(start_date, end_date)
    cron_count_data_daily()
