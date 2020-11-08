# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 11:48
# @Author  : Zhanggd
# @FileName: ReCase1.py
# @Software: PyCharm
# @Blog    ：https://github.com/ZhanggdRunner

import requests

# r = requests.get(url="http://www.baidu.com")
# print(r.text)   # 打印返回的正文信息
# print(r.encoding)   # 打印返回的编码
# print(r.url)    # 打印返回的url
# print(r.headers)    # 打印返回的消息头
# print(r.cookies)  # 打印返回的cookie
'''
计算个人的bmi
请求地址：url ="http://www.bmicha.com/"
请求参数：dopost=save&sex=1&height=185&weight=65&typeid=1&arcID=on
请求方式：get
'''
# 方式一，将参数保存在url中
url = "http://www.bmicha.com/?dopost=save&sex=1&height=185&weight=65&typeid=1&arcID=on"
r = requests.get(url=url)
print(r.text)   # 打印响应的正文信息
print(r.headers)  # 打印消息头
print(r.cookies)    # 打印cookie
print(r.url)        #打印url