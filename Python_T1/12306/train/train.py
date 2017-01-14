# -*- coding:utf-8 -*-
import requests
import datetime
import time


def get_query_data():
    resp = requests.get("https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=2016-12-08&from_station=BJP&to_station=SHH", verify=False)
    # 将获取到的数据转化为json格式
    json_resp = resp.json()
    # 数据存储在data里面datas数组中
    r_query_data = json_resp['data']['datas']
    # print query_data
    return r_query_data


def get_seat_data(tic_url, tic_param):
    resp2 = requests.get(tic_url+tic_param, verify=False)
    # resp2 = requests.get("https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no=240000G1010C&from_station_no=01&to_station_no=11&seat_types=OM9&train_date=2016-12-08" ,verify=False)
    # 将获取到的数据转化为json格式
    #print resp2.request.url
    json_resp2 = resp2.json()
    # 数据存储在data里面
    #print json_resp2
    r_seat_data = json_resp2['data']
    print r_seat_data
    return r_seat_data

def get_num_data(no_url, no_param):
    resp3 = requests.get(no_url+no_param, verify=False)
    # resp3 = requests.get("https://kyfw.12306.cn/otn/czxx/queryByTrainNo?train_no=240000G1010C&from_station_telecode=VNP&to_station_telecode=AOH&depart_date=2016-12-08", verify=False)
    # 将获取到的数据转化为json格式
    json_resp3 = resp3.json()
    # 数据存储在data里面
    r_num_data = json_resp3['data']['data']
    # print query_data
    return r_num_data


if __name__ == "__main__":
    # 获取点击查询时返回的数据(数组的形式)
    query_datas = get_query_data()
    # 任意形式的
    # get_query_data((datetime.datatime.now() + datetime.timedelta(days = 3)).strftime("%Y-%m-%d"),"HZH",'VAP')
    # train_no=240000G1010C&from_station_no=01&to_station_no=11&seat_types=OM9&train_date=2016-12-08
    seat_url = "https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice"
    # train_no=240000G1010C&from_station_telecode=VNP&to_station_telecode=AOH&depart_date=2016-12-08
    num_url = "https://kyfw.12306.cn/otn/czxx/queryByTrainNo"
    # 遍历每一个返回的数据，提取其中访问点击余票和车次所需要的信息

    count = 0
    for query_data in query_datas:
        count += 1
        print count
        if count == 2:
            break
        train_no = query_data['train_no'].encode("utf-8")
        from_station_no = query_data['from_station_no'].encode("utf-8")
        to_station_no = query_data['to_station_no'].encode("utf-8")
        seat_types = query_data['seat_types'].encode("utf-8")
        # train_date = query_data['train_date'].encode("utf-8")
        train_date = "2016-12-08"
        from_station_telecode = query_data['from_station_telecode'].encode("utf-8")
        to_station_telecode = query_data['to_station_telecode'].encode("utf-8")
        depart_date = "2016-12-08"

        # seat_param = {"train_no": train_no, "from_station_no": from_station_no, "to_station_no": to_station_no,
        #                 "seat_types": seat_types, "train_date": train_date}
        seat_param = u"?train_no="+train_no + u"&from_station_no="+from_station_no + u"&to_station_no="+to_station_no + u"&seat_types="+seat_types + u"&train_date="+train_date
        # num_param = {"train_no": train_no, "from_station_telecode": from_station_telecode, "to_station_telecode": to_station_telecode,
        #                 "depart_date": depart_date}
        num_param = u"?train_no=" + train_no + u"&from_station_telecode=" + from_station_telecode + u"&to_station_telecode=" + to_station_telecode + u"&depart_date=" + depart_date
        # seat_data 是个对象
        seat_data = get_seat_data(seat_url, seat_param)
        # 返回途径的站点信息，是个数组
        num_datas = get_num_data(num_url, num_param)
        out = ""
        with open(u"北京-上海".encode("utf-8"),"w+") as f:
            out += u"车次 ：".encode("utf-8") + query_data['station_train_code'].encode("utf-8")+'\t'
            out += u"出发站 ：".encode("utf-8") + query_data['from_station_name'].encode("utf-8")+'\t'
            out += u"到达站 ：".encode("utf-8") + query_data['end_station_name'].encode("utf-8")+'\t'
            out += u"出发时间 ：".encode("utf-8") + query_data['start_time'].encode("utf-8")+'\t'
            out += u"到达时间 ：".encode("utf-8") + query_data['arrive_time'].encode("utf-8")+'\t'
            out += u"历时 ：".encode("utf-8") + query_data['lishi'].encode("utf-8")+'\n'
            out += u"商务座 ：".encode("utf-8") + query_data['swz_num'].encode("utf-8")+'\t'
            out += u"特等座 ：".encode("utf-8") + query_data['tz_num'].encode("utf-8")+'\t'
            out += u"一等座 ：".encode("utf-8") + query_data['zy_num'].encode("utf-8")+'\t'
            out += u"二等座 ： ".encode("utf-8") + query_data['ze_num'].encode("utf-8")+'\t'
            out += u"高级卧铺 ：".encode("utf-8") + query_data['gr_num'].encode("utf-8")+'\t'
            out += u"软卧 ：".encode("utf-8") + query_data['rw_num'].encode("utf-8")+'\t'
            out += u"硬卧 ：".encode("utf-8") + query_data['yw_num'].encode("utf-8")+'\t'
            out += u"软座 ：".encode("utf-8") + query_data['rz_num'].encode("utf-8") + '\t'
            out += u"硬座 ：".encode("utf-8") + query_data['yz_num'].encode("utf-8") + '\t'
            out += u"无座 ：".encode("utf-8") + query_data['wz_num'].encode("utf-8")+'\n'

            # out += u"商务座 ：".encode("utf-8") + query_data['swz_num'] + '\t'
            # out += u"特等座 ：".encode("utf-8") + query_data['tz_num'] + '\t'
            # out += u"一等座 ：".encode("utf-8") + query_data['zy_num'] + '\t'
            # out += u"二等座 ： ".encode("utf-8") + query_data['ze_num'] + '\t'
            # out += u"高级卧铺 ：".encode("utf-8") + query_data['gr_num'] + '\t'
            # out += u"软卧 ：".encode("utf-8") + query_data['rw_num'] + '\t'
            # out += u"硬卧 ：".encode("utf-8") + query_data['yw_num'] + '\t'
            # out += u"软座 ：".encode("utf-8") + query_data['rz_num'] + '\t'
            # out += u"硬座 ：".encode("utf-8") + query_data['yz_num'] + '\t'
            # out += u"无座 ：".encode("utf-8") + query_data['wz_num'] + '\n'
            out += u"途经站点".encode("utf-8")+"\n"
            for num_data in num_datas:
                out += num_data['station_name'].encode("utf-8") + '\t'
                out += num_data['arrive_time'].encode("utf-8") + '\t'
                out += num_data['start_time'].encode("utf-8") + '\t'
                out += num_data['stopover_time'] .encode("utf-8") + '\n'

            f.write(out)

