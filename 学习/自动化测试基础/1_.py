"""
环境搭建
selenium + python 自动化测试环境搭建

selenium:
- 开源的
- 跨平台
- 支持多种语言: python java
- 支持多浏览器: 兼容性

环境搭建的需要的内容:
- 浏览器
- 安装selenium
    - python
    - selenium
- 浏览器驱动
    - 浏览器驱动, 通过python启动浏览器, 需要下载相关的驱动
    - 浏览器版本和驱动版本相对应
    - 将下载的驱动解压exe文件, 放到python安装目录下

安装selenium
- pip install selenium
- pip list # 检查pip所有的库

根据自己要使用的浏览器的版本去下载相应版本的驱动
然后将驱动文件放在python安装的根目录下
- where python # 查看python安装路径
直接将.exe文件放在根目录下即可

环境搭建好后, 就可以使用驱动搭建我们的浏览器了

操作步骤:
- 导入selenium
- 打开浏览器
- 输入网址
- 对浏览器进行操作


"""
import time
import webbrowser

from selenium import webdriver

# 打开浏览器
# driver = webdriver.Chrome() # 如果驱动不是在根目录下，则不需要填写， 自定义路径， 则需要（）中填写路径
driver = webdriver.Edge()

# 输入网址:
driver.get("http://baidu.com") # 请求网址

# 对历览器进行操作
time.sleep(1) # 模拟操作

driver.quit() # 关闭浏览器







