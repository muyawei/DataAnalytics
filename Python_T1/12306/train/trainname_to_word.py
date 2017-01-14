# -*- coding : utf-8 -*-
import requests

if __name__ == "__main__":
    s = requests.get("https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8983", verify=False)
    datas = s.content
    sp_datas = datas.split('@')
    out = ""
    for i in range(1, len(sp_datas)):
        sp_data = sp_datas[i]
        datas = sp_data.split('|')
        out += datas[1] + "\t"
        out += datas[2] + "\n"
    with open("train_name.txt", "w+") as f:
            f.write(out)
