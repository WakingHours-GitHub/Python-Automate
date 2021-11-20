import datetime

print((datetime.datetime.now() - datetime.datetime(1, 1, 1)).days)



date = datetime.datetime.now()  # 返回datetime对象
day = date.strftime("%Y-%m-%d")  # 获取年月日
times = date.strftime("%H:%M")  # 获取当前时间 # 也可以修改为自定义时间
day_R = date.strftime("%d")
segment = 1298510  # 加密参数 # 应该模拟加密过程 # 模拟的参数, 正常加密过程没做完
# 1298527
segment = segment + int(day_R)
print(segment)