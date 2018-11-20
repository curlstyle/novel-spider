# -*- coding: UTF-8 -*-
import urllib
from bs4 import BeautifulSoup
from xlwt import *  
import random

url = 'http://www.biquge.com.tw/0_552/412578.html'
text_url = url

user_agent ='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
headers_test = {'User-Agent':user_agent}
proxy = {'http':'http://121.49.110.65:8888'}
proxy_handler = urllib.request.ProxyHandler(proxy)
opener = urllib.request.build_opener(proxy_handler)
urllib.request.install_opener(opener)
text_request = urllib.request.Request(text_url,None,headers_test)  
text_response = urllib.request.urlopen(text_request,None,timeout=10)
text_html = text_response.read().decode('gbk','ignore')
# try:
# 	text_request = urllib.request.Request(text_url,None,headers)  
# 	text_response = urllib.request.urlopen(text_request,None,timeout=10)
# 	try:
# 		text_html = text_response.read().decode('gbk')
# 	except Exception as e:
# 		print("读取网页失败，正在尝试重新读取!")
# 		text_html = text_response.read().decode('gbk')
# except Exception as e:
# 	print("连接请求失败，正在尝试重新连接!")
# 	text_request = urllib.request.Request(text_url,None,headers)  
# 	text_response = urllib.request.urlopen(text_request,None,timeout=10)
# 	try:
# 		text_html = text_response.read().decode('gbk')
# 	except Exception as e:
# 		print("读取网页失败，正在尝试重新读取!")
# 		text_html = text_response.read().decode('gbk')

print(text_html)
# text_soup = BeautifulSoup(text_html, "html.parser")
# print(text_soup)
# text_context = text_soup.find(name='div',attrs={"id":'content'}).get_text('\n','br/')
# # text_context = text_context[:-56]
# text_title = text_soup.h1.get_text()
# print(text_title)
# print(text_context)
# print("正在写入： "+ text_title)
# fileHandle.write (text_title+'\n\n'+text_context+'\n\n')

# fileHandle.close()