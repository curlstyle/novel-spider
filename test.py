# no=[0,1,2,3,4]
# try:
# 	print(no.index(2))
# except ValueError as v:
# 	print('1111')
# else:
# 	print('22222')

import urllib
from bs4 import BeautifulSoup
from xlwt import *  
import random
headers = {'Accept': '*/*',
           'Accept-Language': 'en-US,en;q=0.8',
           'Cache-Control': 'max-age=0',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
           'Connection': 'keep-alive',
           'Referer': 'http://www.biquge.com.tw/'
           }
catalogue_url_list = []
catalogue_url='http://www.biquge.com.tw/12_12422/'
catalogue_request = urllib.request.Request(catalogue_url,None,headers)  
catalogue_response = urllib.request.urlopen(catalogue_request,None)
catalogue_html = catalogue_response.read().decode('gbk')
catalogue_soup = BeautifulSoup(catalogue_html, "html.parser")
catalogue_list = catalogue_soup.find(name='div',attrs={"id":'list'}).find_all('a')
for item in catalogue_list:
	catalogue_url_list.append(item.get('href'))


print(catalogue_url_list)