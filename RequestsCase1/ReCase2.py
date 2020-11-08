# -*- coding: utf-8 -*-
# @Time    : 2020/10/26 22:42
# @Author  : Zhanggd
# @FileName: ReCase2.py
# @Software: PyCharm
# @Blog    ：https://github.com/ZhanggdRunner
# 针对https协议，这里以携程网为例
import requests
url = "https://www.ctrip.com/"
r = requests.get(url=url,verify=True)
print(r.text)
# 解决方案：在发送请求时忽略证书，证书的参数是verify
