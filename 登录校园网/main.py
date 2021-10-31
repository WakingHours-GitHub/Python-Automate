import requests
import os

url = "http://172.17.100.10/a79.htm?wlanuserip=10.200.170.201&wlanacname=me60&me60ip=172.16.255.100&wlanusermac=0c-dd-24-76-92-79"

headers = {

}

params = {

}

resp = requests.post(url, headers=headers, params=params)
if resp:
    print("登录成功")
else:
    print("登录失败")

os.system("pause")  # 暂停
