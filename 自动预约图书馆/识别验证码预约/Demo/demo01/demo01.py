import sys
import ddddocr
import requests  # 用于进行访问
import re  # re 模块, 用于正则匹配
import time
from selenium import webdriver  # 浏览器驱动
from selenium.webdriver.common.by import By # 元素定位对象
import datetime  # 日期, 时间相关
import cv2
import numpy as np


# 获取5A的URL
# 未解决的问题: segment仍然是仿真值, 没有模拟过程
def getFive_A_URL():
    """
    :param: None
    :dic
    :return:
    """
    date = datetime.datetime.now()  # 返回datetime对象
    day = date.strftime("%Y-%m-%d")  # 获取年月日
    times = date.strftime("%H:%M")  # 获取当前时间 # 也可以修改为自定义时间
    day_R = date.strftime("%d")  # 获取当前 :日 (号)

    # 对日期做计算
    delta = datetime.timedelta(days = 1)
    dateOfReservation = date + delta  # 得到的是后一天的时间
    print(dateOfReservation.strftime("%Y-%m-%d"))  # 后一天


    # print(day_R)
    # print(day)

    # 参数部分:
    segment = 1298510  # 具体还没有模拟
    # 用于确定日期天数
    segment = segment + int(day_R) + 1  # 预约的是明天五楼A, 参数是仿(模拟)的

    # print("segment -> ", segment)
    # 2021.11.18访问5楼室内
    # "http://222.27.188.3/web/seat3?area=29&segment=1297994&day=2021-11-19&startTime=06:00&endTime=22:00"

    # 拼接url:


    Five_A_URL = "http://222.27.188.3/web/seat3?area=30&segment=" + str(segment) + "&day=" + str(
        dateOfReservation.strftime("%Y-%m-%d")) + "&startTime=06:00&endTime=22:00"
    Five_A_URL = Five_A_URL.replace(" ", "")

    print("Five_A_URL -> ", Five_A_URL)

    return Five_A_URL


# 获取验证码部分:
def getVerificationCode(driver):
    # 定位截图：
    img = driver.find_element(By.XPATH, "/html/body/div[11]/div/table/tbody/tr[2]/td/div/div/div[3]/img")
    img.screenshot("test2.png")

    cv2img = cv2.imread("test2.png")
    cv2img = cv2.cvtColor(cv2img, cv2.COLOR_RGB2GRAY)
    # ret, binary = cv2.threshold(cv2img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # 中位值降噪
    # dst = cv2.medianBlur(cv2img, 5)
    # cv2.imshow("median_blur_demo", dst)
    # 自定义降噪 -> 原理不明白
    kernel = np.array(
        [[0, -1, 0],
         [-1, 4.85, -1],
         [0, -1, 0]],
        np.float32)
    binary = cv2.filter2D(cv2img, -1, kernel=kernel)
    # erode = cv2.erode(binary, None, iterations=1)

    # cv2.imwrite("test3.png", cv2img)
    cv2.imwrite("test3.png", binary)
    # cv2.waitKey(0)

    with open("test3.png", "rb") as f:
        imgBuff = f.read()

    ocr = ddddocr.DdddOcr()
    cood = ocr.classification(imgBuff)
    print(cood)
    return cood


# 下面代码是一开始的想法, 但是是不可行的
'''
def getVerificationCode():
    """
    因为无法直接访问/api/check (验证不是服务器访问, 所以拒绝访问)
    所以我们需要带上Referer -> 防盗链. 发送请求, 然后获取check的响应字节流
    返回的相应字节流是bin文件 -> 其实是一个png格式的二进制流, 然后我们用ddddocr来破解, 返回验证码即可
    
    :return: cood
    """
    checkURL = "http://222.27.188.3/api.php/check"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53",
        "Referer": "http://222.27.188.3/home/web/seat/area/1" # -> 添加防盗链
    }
    resp = requests.get(checkURL, headers=headers) # 访问

    with open("test.png", "wb") as f:
        f.write(resp.content)
    ocr = ddddocr.DdddOcr()  # -> 实例化对象
    print(ocr.classification(resp.content))
        
    return ocr.classification(resp.content)
    

    pass
'''


def login(user, driver):
    while True:
        # 进行用户登录:
        # 输入用户名, 密码, 和验证码
        try:
            # "/html/body/div[11]/div/table/tbody/tr[2]/td/div/div/div[1]/input" 折叠和展开好像是一样的 2021.11.16
            driver.find_element(By.XPATH, "/html/body/div[11]/div/table/tbody/tr[2]/td/div/div/div[1]/input").send_keys(
                user["username"])
            driver.find_element(By.XPATH, "/html/body/div[11]/div/table/tbody/tr[2]/td/div/div/div[2]/input").send_keys(
                user["password"])
            time.sleep(2)

            driver.find_element(By.XPATH, "/html/body/div[11]/div/table/tbody/tr[2]/td/div/div/div[3]/input").send_keys(
                str(getVerificationCode(driver)))
            break
        except:
            print("登录界面找到")

    time.sleep(5)

    # 点击登录, -> 需要判断是否登录成功
    while True:
        try:
            driver.find_element(By.XPATH, "/html/body/div[11]/div/table/tbody/tr[3]/td/div[2]/button[2]").click()
            break
        except:
            pass

    # 关掉: 登录成功提示和预约规则
    while True:
        try:
            driver.find_element(By.XPATH, "/html/body/div[14]/div/table/tbody/tr[1]/td/button").click()
            break
        except:
            pass

    while True:
        try:
            driver.find_element(By.XPATH, "/html/body/div[11]/div/table/tbody/tr[3]/td/div[2]/button").click()
            break
        except:
            pass



def run():
    # 创建用户字典
    # 当前是一个用户, 后面可做成多线程, 或者迭代的版本
    users = {
        "name": "FWJ",
        "username": "201923020986",
        "password": "fwj201923020986"
    }

    # 启动浏览器,进行预约
    driver = webdriver.Edge()  # 启动浏览器

    driver.get(getFive_A_URL())  # 访问五楼A

    while True:
        try:
            # 点击登录界面
            # 利用try-except进行判断分割
            try:
                # 折叠
                driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/ul/li[6]/a").click()
            except:
                # 全屏
                driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/ul/li[4]/a").click()

            # "/html/body/div[3]/div[1]/ul/li[6]/a"  "user-profile dropdown-toggle login-btn login_click"# 折叠
            # "/html/body/div[2]/div[1]/ul/li[4]/a"  "login-btn login_click"  # 全屏

            break

        except:
            print("无法找到登录按钮, 请等待")

    print("点击完了登录按钮")  # 测试用

    # 下面进行登录操作 -> sentKey(输入)和破解验证码
    login(users, driver)



    # 登陆完, 要进行座位判断和获取
    """
        两种版本
        -> 可以做全盘扫描, 哪里有地方, 选哪  -> 需要全局扫描
        -> 指定座位列表, 按照优先级, 选择座位 -> 指定座位列表, 针对作为列表去选座
    """

    time.sleep(1000)  # 暂停


if __name__ == '__main__':
    run()  # 启动运行逻辑
