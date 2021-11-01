# 查看源码, 看需要定位的元素是否有id属性
# 若有, 则需要定位, 若没有则不需要定位
from selenium import webdriver

driver = webdriver.Edge()

driver.get("www.baidu.com")

# 元素定位 -- id
ele = driver.find_element_by_id("")
# 查看定位元素
print(ele.get_attribute("outerHTML"))
# 操作
# 输入
ele.send_keys("") # 以字符串的方式输入
# 当然你也可以使用链式编程的思维

