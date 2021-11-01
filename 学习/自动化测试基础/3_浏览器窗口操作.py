from selenium import webdriver

# 选择浏览器
driver = webdriver.Edge()
# 打开被测网址
driver.get("")

# 对窗口进行相应操作
# 窗口最大化
# driver.maximize_window()

# 指定窗口大小: 宽x, 高y 单位:分辨率
# driver.set_window_size(x,y)



