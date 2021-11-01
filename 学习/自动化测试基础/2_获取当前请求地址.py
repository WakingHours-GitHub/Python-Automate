import time
import webbrowser

from selenium import webdriver

# 打开浏览器
# driver = webdriver.Chrome() # 如果驱动不是在根目录下，则不需要填写， 自定义路径， 则需要（）中填写路径
driver = webdriver.Edge()

# 输入网址:
driver.get("http://baidu.com") # 请求网址

# 对历览器进行操作
# time.sleep(1) # 模拟操作

# 常用操作:
# 获取当前网址
print(driver.current_url) # 打印当前所请求的网址
# 后退
driver.back()
# 前进
driver.forward()
# 刷新
driver.refresh()
# 获取title: HTML中的tile概念
# driver.title
print(driver.title)
# 可与结合断点进行调试, 一步一步往下走

# 以上是对浏览器url进行的一些操作







driver.quit() # 关闭浏览器







