from selenium import webdriver
import datetime
import  time
date = datetime.datetime.now()
hours_min = date.strftime("%H:%M")

home_page = "http://222.27.188.3/home/web/seat/area/1"
Five_A = "http://222.27.188.3/web/seat3?area=30&segment=1298506&day=2021-10-27&startTime="+str(hours_min)+"&endTime=22:00"
Five_A = Five_A.replace(" ", "")
print(Five_A)

driver = webdriver.Edge()

driver.get(Five_A)
driver.maximize_window()
driver.refresh()

time.sleep(1)
# ele = driver.find_element("data-no","6147")
# /html/body/div[6]/div[1]/div[1]/div/ul/li[1]
# ele = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div/ul/li[1]")
# print(ele.get_attribute("outerHTML"))

# 登录:

# driver.find_element_by_class_name("login-btn login_click").click()
# driver.find_element_by_class_name("user-profile dropdown-toggle login-btn login_click").click()
driver.find_element("class","login-control")

# 67号: data-no="6147"