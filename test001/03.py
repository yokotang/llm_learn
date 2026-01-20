import requests
from bs4 import BeautifulSoup
import hashlib
import json
from numpy.ma.core import logical_not

# url = "https://uinajlkdn.jianbai.net/customer/login?isForce=true"

#     # 发送GET请求
# response = requests.get(url)
#     # 断言验证
# assert response.status_code == 200, f"状态码错误: {response.status_code}"
# assert response.headers["Content-Type"] == "application/json; charset=utf-8"
# url = "https://uinajlkdn.jianbai.net/customer/login"
# # 请求体数据
# payload = {
#     "loginName": "admin",
#     "loginPwd": "ulike@2025",
#     "loginType": "1",
#     "appId": "2"
# }
#
# # 发送POST请求
# response = requests.post(url, json=payload)
#
# assert response.status_code == 201  # 创建成功
# data = response.json()
# assert data["title"] == "测试标题"
#
# print("✓ POST请求测试通过")
def md5_encrypt(s: str) -> str:
    return hashlib.md5(s.encode('utf-8')).hexdigest()
login_url="https://uinajlkdn.jianbai.net/customer/login"
user_name="admin"
user_pwd="ulike@2025"
login_pwd = md5_encrypt(user_pwd)
payload = {"body": json.dumps
    ({"loginName": user_name,
        "loginPwd": login_pwd,
        "appId": 2,
        "loginType": 1})}
    # "loginName": user_name,
    # "loginPwd": login_pwd,
    # "appId": 2,
    # "loginType": 1}
headers = {
    "Content-Type": "application/json;charset=UTF-8",
    "Accept": "application/json, text/plain, */*"
}
response = requests.post(login_url, data=payload,headers=headers,timeout=10)
response.raise_for_status()
data=response.json()
print(response.status_code)
