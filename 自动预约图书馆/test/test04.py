import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()


url = "http://222.27.188.3/web/seat3?area=30&segment=1298506&day=2021-10-27&startTime=19:26&endTime=22:00"


driver.get(url)

# driver.find_element_by_class_name("login-control").click() # 已经被弃用

postURL = "http://222.27.188.3/api.php/login"
headers={
    "User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30",
    "Cookie": "PHPSESSID=hj3f08e5vok66pe6qd0th7cme3",
    "Referer":" http://222.27.188.3/web/seat3?area=30&segment=1298506&day=2021-10-27&startTime=19:26&endTime=22:00"

}
params={

}


session = requests.Session()
# resp = session.post(postURL, headers=headers, params=)


time.sleep(1)
driver.maximize_window()
driver.refresh()

driver.find_element(By.CLASS_NAME, "login-control").click()




# time.sleep(100)

# 登录
#


# 点击座位:
while 1:
    driver.find_element("data-no","6081").click()

