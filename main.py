import requests
import json

from config_loader import load_headers
from input_validation import prompt_date, prompt_station


# 地点转代码
with open("12306_station_name_to_code.json", "r", encoding="utf-8") as file:
    stations = json.load(file)

# 用户输入
date = prompt_date()
from_station_code = prompt_station(stations, "出发站")
to_station_code = prompt_station(stations, "目的地")


# 12306的查询接口
url = (
    "https://kyfw.12306.cn/otn/leftTicket/queryG?"
    f"leftTicketDTO.train_date={date}&"
    f"leftTicketDTO.from_station={from_station_code}&"
    f"leftTicketDTO.to_station={to_station_code}&"
    "purpose_codes=ADULT"
)

# 从本地配置读取隐私请求头
headers = load_headers()


# 获取数据
response = requests.get(url, headers=headers)


# 遍历信息
for i in response.json()["data"]["result"]:
    f = i.split("|")
    print(f"车辆名称:{f[3]}|起始时间:{f[8]}|到达时间:{f[9]}|一等座:{f[31]}|二等座:{f[30]}|无座:{f[26]}")
