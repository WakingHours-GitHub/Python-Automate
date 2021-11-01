import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import requests
import re

date = datetime.datetime.now()  # 返回datetime对象
day = date.strftime("%Y-%m-%d")  # 获取年月日
times = date.strftime("%H:%M")  # 获取当前时间 # 也可以修改为自定义时间
day_R = date.strftime("%d")
# print(day_R)

# print(day, times)
segment = 1298510  # 加密参数 # 应该模拟加密过程 # 模拟的参数, 正常加密过程没做完
segment = segment + int(day_R)
print(segment)

username = "201923020986"
password = "fwj201923020986"
code = "0000"  # 验证码
seats = [122, 121, 62, 61, 65, 66]

# url = "http://222.27.188.3/web/seat3?area=30&segment=1298506&day=2021-10-27&startTime=19:26&endTime=22:00"
Five_A = "http://222.27.188.3/web/seat3?area=30"
# &segment=1298507&day=2021-10-28&startTime=14:29&endTime=22:00
# http://222.27.188.3/web/seat3?area=30&segment=1298508&day=2021-10-29&startTime=12:43&endTime=22:00
Five_A = (Five_A + "&segment=" + str(segment) + "&day=" + str(day) + "&startTime=" + str(times) + str(
    "&endTime=22:00")).replace(" ", "")  # 格式化赋值

print(Five_A)

driver = webdriver.Edge()  # 启动浏览器

driver.get(Five_A)  # 请求页面

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Content-Length": "58",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    'Cookie': "PHPSESSID=45fie6q6b3d2emdfivom6ir8t1; uservisit=0; redirect_url=%2Fhome%2Fweb%2Fseat%2Farea%2F1; userid=201923020986; user_name=%E8%8C%83%E7%8E%AE%E5%98%89; access_token=23712187ec3c70ca000320acc030b9ba; expire=2021-10-28+14%3A51%3A06",
    'Host': "222.27.188.3",
    'Origin': "http://222.27.188.3",
    # 'Referer': "http://222.27.188.3/web/seat3?area=30&segment=1298507&day=2021-10-28&startTime=14:38&endTime=22:00",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30"
}

data = {
    "Pragma": "no-cache",
    "Server": "nginx-upupw/1.18.0-iocp",
    "Set-Cookie": "userid=201923020986; path=/",
    # "Set-Cookie": "user_name=%E8%8C%83%E7%8E%AE%E5%98%89; path=/",
    # "Set-Cookie": "access_token=88b60d8214b427dd5bed50473830e196; path=/",
    # "Set-Cookie": "expire=2021-10-28+14%3A58%3A02; path=/"
}

session = requests.session()

# resp = session.post(Five_A,data=data,headers=headers) # post请求

driver.refresh()  # 刷新

driver.maximize_window()  # 最大化窗口

# 定位元素: 登录
while 1:
    try:
        # 点击登录界面
        driver.find_element(By.CLASS_NAME, "login-control").click()  # 点击登录界面
        # 输入用户名和密码
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        # 输入验证码
        time.sleep(5)  # 这里用等待模拟
        break

    except Exception:
        print("登录界面没有找到")

# 点击确定. 进入到登录界面
driver.find_element(By.CLASS_NAME, "ui-dialog-autofocus").click()

# 然后开始执行, 关掉界面, 开始预约座位等步骤

# 关掉提醒页面
while 1:
    try:
        driver.find_element(By.CLASS_NAME, "ui-dialog-autofocus").click()  # 关闭提醒界面
        break

    except Exception:
        print("未删除提醒界面")

# 开一个re对象


# "/html/body/div[6]/div[1]/div[1]/div/ul/li[11]" # 北A11
# "/html/body/div[6]/div[1]/div[1]/div/ul/li[65]" # 北A65
# 规律: ul -> li [x] .x 代表座位

# 预约座位, 这里使用XPATH进行元素定位
for seat in seats:
    success = 0
     # 拼接XPATH
    XPATH = "/html/body/div[6]/div[1]/div[1]/div/ul/li[" + str(seat) + "]"
    XPATH.replace(" ", "")  # 清除空格 # 格式化
    print(XPATH) # 打印

    while 1:
        try:
            # 北A65号座位
            ele = driver.find_element(By.XPATH, XPATH)
            txt = str(ele.get_attribute("outerHTML"))

            # print(str(ele.get_attribute("outerHTML")))
            # 使用正则表达式匹配状态: state
            state = re.search(r"&quot;status_name&quot;:&quot;(?P<state>.*?)&quot;", txt).group("state")
            # 比较返回的状态
            if state == "空闲":
                ele.click()  # 若是空闲, 则点击
                # 点击完座位后, 确认预约
                while True:
                    try:
                        # 点击确认预          约
                        driver.find_element(By.CLASS_NAME,"ui-dialog-autofocus").click()
                        # 预约成功
                        print(f"{seat}号座位, 预约成功")
                        success = 1 # 预约成功 # 预约到一个位置, 就算成功, 于是就不再预约下面的内容,直接退出

                        break
                    except Exception:
                        print("预约失败")
                        success = 0

            # 其他状况
            else:
                print(f"第{seat}号座位, 无法预约, 正在迭代下一次座位")

            break
        except Exception:
            print("没有座位")
    if success == 1:
        break # 预约成功, 跳出




# time.sleep(100)  # 测试用

driver.quit()  # 退出
