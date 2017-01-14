获取所有代售点的信息

首先查看代售点页面--->network 发送了一个allProvince的请求
               ----> 返回一个json对象，对象中data中存储一个json数组，json数组中每个json对象的chineseName为省份名称

在代售点页面中选择省份--->network发送了一个https://kyfw.12306.cn/otn/queryAgencySellTicket/queryAgentSellCity?province=安徽  的请求
                   ---> 返回一个json对象，对象中data中存储一个数组，数组中每个元素为省份的市的名称

在代售点页面中选择市  --->network发送了一个https://kyfw.12306.cn/otn/queryAgencySellTicket/queryAgentSellCounty?province=安徽&city=濠州 的请求
                   ---> 返回一个json对象，对象中data中存储一个数组，数组中每个元素为市下的区县名称

在代售点页面中选择区／县  --->network发送了一个https://kyfw.12306.cn/otn/queryAgencySellTicket/queryAgentSellCounty?province=安徽&city=濠州&county=六安市 的请求
                   ---> 返回一个json对象，对象中data中存储一个对象，对象中datas为代售点的具体信息

为获得相同的页面，需要进行级联的操作

先从allProvince请求中获取所有的省份信息，
依次进行拼接，获取每个省份的市
在依次拼接，获取市的区县
继续拼接获取区县下的代售点信息


我们尝试发现，省，市，县都不进行选择的时候会报错，而进行选择省的时候，该省的所有代售点会列举出来
所以只为了获取全部数据，我们可以直接进行省的选择，获取某个省的全部数据，而省去市、区的操作
{"validateMessagesShowId":"_validatorMessage","status":true,"httpstatus":200,
"data":{"datas":[{"bureau_code":"G","station_telecode":"JJG","belong_station":"九江","province":"安徽","city_code":"","city":"安庆",
                  "county":"宿松县","windows_quantity":"1","agency_name":"宿松县汇口镇代售点",
                  "address":"安徽省宿松县汇口镇德化路64号","addressencode":"%B0%B2%BB%D5%CA%A1%CB%DE%CB%C9%CF%D8%BB%E3%BF%DA%D5%F2%B5%C2%BB%AF%C2%B764%BA%C5","phone_no":"0556-7580222","start_time_am":"0730","stop_time_am":"1200","start_time_pm":"1200","stop_time_pm":"1830"},
                 {"bureau_code":"G","station_telecode":"JJG","belong_station":"九江","province":"安徽","city_code":"","city":"安庆",
                  "county":"宿松县","windows_quantity":"1","agency_name":"宿松县宿松路代售点",
                  "address":"安徽省宿松县孚玉镇宿松路211号（汽车站旁）","addressencode":"%B0%B2%BB%D5%CA%A1%CB%DE%CB%C9%CF%D8%E6%DA%D3%F1%D5%F2%CB%DE%CB%C9%C2%B7211%BA%C5%A3%A8%C6%FB%B3%B5%D5%BE%C5%D4%A3%A9","phone_no":"0556-7818730","start_time_am":"0800","stop_time_am":"1200","start_time_pm":"1400","stop_time_pm":"1830"},


*************************
因为返回的是json数据，所以不需要解析器
*************************

