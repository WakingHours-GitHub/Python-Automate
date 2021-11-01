import time

from selenium import webdriver
import datetime  # 日期
import requests

day = datetime.date.today()
date = datetime.datetime.now()
hours = date.strftime("%H:%M")
print(hours)
print(day)

home = "http://222.27.188.3/home/web/seat/area/1"
FiveLayers = "http://222.27.188.3/web/seat2/area/6/day/"  # + 2021-10-26(日期)
Five_North_A = "http://222.27.188.3/web/seat3?area=30"
# http://222.27.188.3/web/seat3?area=30&day=2021-10-27&startTime=15:09&endTime=22:00
# http://222.27.188.3/web/seat3?area=30&segment=1298506&day=2021-10-27&startTime=15:17&endTime=22:00
# http://222.27.188.3/web/seat3?area=30 &segment=1298506&day=2021-10-27&startTime=15:10&endTime=22:00
FiveLayers = (FiveLayers + str(day)).replace(" ", "")  # 替换并且合并
print(FiveLayers)

Five_North_A = Five_North_A + "&segment=1298506" + "&day" + str(day) + "&startTime=" + str(hours) + "&endTime=22:00"
Five_North_A = Five_North_A.replace(" ", "")  # 替换空格
print(Five_North_A)

postURL = "http://222.27.188.3/api.php/login"
session = requests.session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30",
    # "Referer": "http://222.27.188.3/web/seat3?area=30&segment=1298506&day2021-10-27&startTime=15:19&endTime=22:00"
}
params={
    "Cookie": "PHPSESSID=p422i28d1g30527c0otp0hoql0; redirect_url=%2Fhome%2Fweb%2Fseat%2Farea%2F1"
}
# resp = session.get(postURL, headers=headers, params=params)

driver = webdriver.Edge()  # 打开浏览器

driver.get(Five_North_A)  # 打开页面
resp = session.get(Five_North_A, headers=headers, params=params)
driver.refresh()
driver.maximize_window()

# driver.find_element_by_class_name("btn btn-default active area_day").click()


time.sleep(100)


# driver.quit()
