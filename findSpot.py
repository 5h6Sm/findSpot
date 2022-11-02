# http://openapi.seoul.go.kr:8088/(인증키)/xml/GetParkInfo/1/5/
# 78566558566c696d35337144614a64

# import requests
# import pandas as pd
# import math

# API_KEY = "78566558566c696d35337144614a64"
# url=f'http://openapi.seoul.go.kr:8088/{API_KEY}/json/GetParkInfo/1/2/'
# re=requests.get(url)
# rjson=re.json()
# total_num=int(rjson['GetParkInfo']['list_total_count'])

# parking_name=[]
# pay_yn=[]
# full_month_fee=[]
# rates=[]
# time_rates=[]
# lat=[]
# long=[]
# cap=[]
# holiday=[]

# for i in range(1, math.ceil(total_num/1000)+1):

#     end=i*1000
#     start=end-1000 +1

#     if end >total_num:
#         end = total_num

#     url=f'http://openapi.seoul.go.kr:8088/{API_KEY}/json/GetParkInfo/{start}/{end}'
#     re=requests.get(url)
#     rjson=re.json()

#     for u in rjson['GetParkInfo']['row']:
#         parking_name.append(u['PARKING_NAME'])
#         pay_yn.append(u['PAY_NM'])
#         full_month_fee.append(u['FULLTIME_MONTHLY'])
#         rates.append(u['RATES'])
#         time_rates.append(u['TIME_RATE'])
#         lat.append(u['LAT'])
#         long.append(u['LNG'])
#         cap.append(u['CAPACITY'])
#         holiday.append(u['HOLIDAY_PAY_NM'])


# import requests
# import pprint
# import json

# url = 'http://api.data.go.kr/openapi/tn_pubr_public_cctv_api?serviceKey=78566558566c696d35337144614a64&pageNo=1&numOfRows=10&type=json'

# response = requests.get(url)

# contents = response.text

# import requests
# import pprint
# import json
# import pandas as pd

# url = 'http://api.data.go.kr/openapi/tn_pubr_public_cctv_api?serviceKey=78566558566c696d35337144614a64&pageNo=1&numOfRows=10&type=json'

# response = requests.get(url)

# contents = response.text

# pp = pprint.PrettyPrinter(indent=4)
# print(pp.pprint(contents))

# json_ob = json.loads(contents)

# body = json_ob['response']['body']['items']
# print(body)

# dataframe = pd.json_normalize(body)

# print(dataframe)

# http://openapi.seoul.go.kr:8088/(인증키)/xml/GetParkInfo/1/5/
# 78566558566c696d35337144614a64

import json
import requests

# 구 이름 입력
# 해당 구에 해당하는 API 상의 데이터(주차장 명) 가져오기
# 무료인지 유료인지 선택받기 -> [유료/무료 선택] or 상관없다
# 평일 -> 시간대 입력받기 -> 사용가능한 시간대인지 확인(야간이라면 +야간무료개방여부 확인) -> 평일 운영 시간에 적합한 시간이면 1
# 토요일이라면? -> 토요일 유, 무료 구분 -> 사용하시겠습니까? -> 시간대 입력받기 -> 주말 운영 시간에 적합한 시간이면 1
# 공휴일이라면? -> 공휴일 유,무료 구분 -> 사용하시겠습니까? -> 시간대 입력받기 -> 공휴일 운영 시간에 적합한 시간이면 1
# 예상 주차 시간 입력 : 기본 주차 요금, 기본 주차 시간(분 단위), 추가 단위 요금, 추가 단위 시간(분 단위) -> 예상 금액 출력 -> 일 최대 금액이라면? 최대 금액 출력
# 원하는 옵션과 일치하는 주차장 명 출력하기

# 데이터 내의 중복 제거(같은 이름의 주차장 제거)
# GPS + 잔여 주차 대수 + 총 주차 가능 수

# 주차 가능 면수 확인 할 수 있는 주차장 API 서울시 실시간 도시데이터
# https://data.seoul.go.kr/dataList/OA-21285/A/1/datasetView.do

# API 두 개 연결해서 사용
# http://data.seoul.go.kr/dataList/OA-21285/A/1/datasetView.do
# http://openapi.seoul.go.kr:8088/4c655649426c696d3130386849544c42/json/citydata/1/100/
# 4c655649426c696d3130386849544c42
# CPCTY 수용가능한 주차대수 / CUR_PRK_CNT 검색하기 / 나와있는 주차장도 있고 없는 주차장도 있음

inputArea = input()
API_KEY = "78566558566c696d35337144614a64"

url = f'http://openapi.seoul.go.kr:8088/{API_KEY}/json/GetParkInfo/1/500/{inputArea}'
son = requests.get(url)
rjson = son.json()

parking_name = []  # 주차장 명
pay_yn = []
full_month_fee = []
rates = []
time_rates = []
lat = []
long = []
cap = []
holiday = []

for u in rjson['GetParkInfo']['row']:
    parking_name = u['PARKING_NAME']
    print(parking_name)
    pay_yn.append(u['PAY_NM'])
    full_month_fee.append(u['FULLTIME_MONTHLY'])
    rates.append(u['RATES'])
    time_rates.append(u['TIME_RATE'])
    lat.append(u['LAT'])
    long.append(u['LNG'])
    cap.append(u['CAPACITY'])
    holiday.append(u['HOLIDAY_PAY_NM'])


print()
