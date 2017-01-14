页面的分析思路：1. 对于html直观显示的页面，分析所要获取数据的位置，利用解析器进行解析即可
              2。对于非html页面，需要用户动态进行选择的页面，利用开发者工具，分析每一次点击所发出的请求，以及返回的数据。对数据进行获取解析
                1）首先分析出页面会提供给我们什么样的数据
                2）每次点击的发出请求，请求的url中个参数从哪来（经常是在上一请求的某个字段包含），什么规律，进行分析
                3）对于返回的数据进行分析

对于12306来说：余票查询页面，票价查询和列车时刻表查询的内容，显示数据基本一致
              在这三个当中余票查询的页面数据是最全的，所需的查询条件也相对于票价查询少，所以为了获取数据，我们从余票查询页面获取

           ---》点击查询时----对于余票页面的分析中，返回的json字段过多，并不知道什么意思，可通过查看源码进行分析。
              https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=2016-12-08&from_station=BJP&to_station=SHH
              返回数据
              {"validateMessagesShowId":"_validatorMessage","status":true,"httpstatus":200,
                "data":{"datas":[{"train_no":"240000G1010C","station_train_code":"G101","start_station_telecode":"VNP",
                                  "start_station_name":"北京南","end_station_telecode":"AOH","end_station_name":"上海虹桥",
                                  "from_station_telecode":"VNP","from_station_name":"北京南","to_station_telecode":"AOH",
                                  "to_station_name":"上海虹桥","start_time":"06:44","arrive_time":"12:38","day_difference":"0",
                                  "train_class_name":"","lishi":"05:54","canWebBuy":"Y","lishiValue":"354",
                                  "yp_info":"IlQNMo8BC0Ox%2Fv1VzQq7o2HG8%2B5ZsIHeEWdEusns7ECs%2B%2BC3",
                                  "control_train_day":"20301231","start_train_date":"20161208","seat_feature":"O3M393",
                                  "yp_ex":"O0M090","train_seat_feature":"3","seat_types":"OM9","location_code":"P2",
                                  "from_station_no":"
                                  ","to_station_no":"11","control_day":29,"sale_time":"1230",
                                  "is_support_card":"1","note":"","controlled_train_flag":"0","controlled_train_message":"正常车次，不受控",
                                  "gg_num":"--","gr_num":"--","qt_num":"--","rw_num":"--","rz_num":"--","tz_num":"--","wz_num":"--",
                                  "yb_num":"--","yw_num":"--","yz_num":"--","ze_num":"354","zy_num":"60","swz_num":"18"}

           ---》点击座位信息时---会比点击查询多了票价信息
              https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no=240000G1010C&from_station_no=01&to_station_no=11&seat_types=OM9&train_date=2016-12-08
              返回的数据
              {"validateMessagesShowId":"_validatorMessage","status":true,"httpstatus":200,
               "data":{"OT":[],"WZ":"¥553.0","M":"¥933.0","A9":"¥1748.0","9":"17480","O":"¥553.0","train_no":"240000G1010C"},
               "messages":[],"validateMessages":{}}

           ---》点击车次时 ----会出现途径站点等信息
              https://kyfw.12306.cn/otn/czxx/queryByTrainNo?train_no=240000G1010C&from_station_telecode=VNP&to_station_telecode=AOH&depart_date=2016-12-08
              返回的数据
              {"validateMessagesShowId":"_validatorMessage","status":true,"httpstatus":200,
               "data":{"data":[{"start_station_name":"北京南","arrive_time":"----","station_train_code":"G101","station_name":"北京南","train_class_name":"高速","service_type":"1","start_time":"06:44","stopover_time":"----","end_station_name":"上海虹桥","station_no":"01","isEnabled":true},
                               {"arrive_time":"07:35","station_name":"沧州西","start_time":"07:38","stopover_time":"3分钟","station_no":"02","isEnabled":true}
                               {"arrive_time":"08:05","station_name":"德州东","start_time":"08:13","stopover_time":"8分钟","station_no":"03","isEnabled":true}

           可以发现点击座位信息和点击车次信息时所发出的url都可以从点击查询时的返回数据当中获取到

           *************************
           查询时不可以用字典，顺序是乱的，会报错！！！
           注意条件不符合时的输出
           *************************


           后经查找发现，车站与对应的字母表示在https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8983这个js文件中
           对文件进行提取数据


           ======================
           若直接进行遍历，会出现重复数据
           全部迭代数据量过大----一次有300多万数据（首次为避免遗漏数据，需要进行完全迭代）
           有的站点之间不存在路线---将存在路线的站点存贮在一个文件中，下次可以避免重复迭代
           =======================


           ********* 发现向导（输入站点，输出所有经过站点的数据，只需所有站点都遍历一遍）--》需要验证码
           https://kyfw.12306.cn/otn/queryTrainInfo/query?leftTicketDTO.train_no=250000S91703&leftTicketDTO.train_date=2016-12-08&rand_code=3Dn4

           ========================
           去查询车次的页面，插卡其js文件，查找里面的ajax请求，因为一般获取数据都是通过ajax，然后查看请求参数（查找$.ajax）

           发现可以获得train_no 和station_train_code --->通过它求出经过站点信息（还缺两个站点代码，不过有站点名，可以通过映射，获取站点代码）=====》提取站点对
           对站点组合进行迭代 =====》获取所有的票价信息