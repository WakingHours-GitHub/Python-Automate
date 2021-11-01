import time

from selenium import webdriver
from selenium.webdriver.common.by import By

username = "201923020986"
password = "fwj201923020986"

seat = ["6146",]

driver = webdriver.Edge()

url = "http://222.27.188.3/web/seat3?area=30&segment=1298506&day=2021-10-27&startTime=19:26&endTime=22:00"
# 2021-10-28: http://222.27.188.3/web/seat3?area=30&segment=1298507&day=2021-10-28&startTime=07:47&endTime=22:00


driver.get(url)

driver.maximize_window()

while 1:
    try:
        driver.find_element(By.CLASS_NAME, "login-control").click()
        # driver.find_element(By.CLASS_NAME, "user-profile dropdown-toggle login-btn login_click").click()

        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        break
    except Exception:
        print("等待")

# 输入用户名和密码

# 输入验证码
time.sleep(10)

# code = 0
#
# while 1:
#     try:
#         driver.find_element(By.NAME,"verify").send_keys(code)
#         break
#     except Exception:
#         print("输入验证码")


driver.find_element(By.CLASS_NAME, "ui-dialog-autofocus").click()



while 1:
    try:
        driver.find_element(By.CLASS_NAME, "ui-dialog-close").click()
        # driver.find_element(By.CLASS_NAME, "ui-dialog-close").click()
        break
    except Exception:
        print("等待")




while 1:
    try:
        driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[1]/div/ul/li[65]").click()
        break
    except Exception:
        print("没有座位")


while 1:
    try:
        driver.find_element(By.CLASS_NAME, "ui-dialog-autofocus").click()
        print("预约成功")
        break
    except Exception:
        print('预约失败')