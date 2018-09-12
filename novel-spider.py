import urllib
from bs4 import BeautifulSoup
from xlwt import *  
import random

book_name=""
book_num=""
catalogue_url_list=[]
book_name = input("请输入书名:")

book_name1 = urllib.parse.quote(book_name.encode('gb2312'))
url = "https://www.ybdu.com/modules/article/search.php?searchtype=keywords&entry=1&searchkey="+book_name1

print(url)
headers = {'Accept': '*/*',
           'Accept-Language': 'en-US,en;q=0.8',
           'Cache-Control': 'max-age=0',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
           'Connection': 'keep-alive',
           'Referer': 'http://www.xicidaili.com/nn'
           }

try:
	request = urllib.request.Request(url,None,headers)
	response = urllib.request.urlopen(request,None,timeout=10)
	try:
		html = response.read().decode('gbk','ignore').encode('utf-8')
	except Exception as e:
		print("读取网页失败，正在尝试重新读取!")
		html = response.read().decode('gbk','ignore').encode('utf-8')
except Exception as e:
	print("连接请求失败，正在尝试重新连接!")
	request = urllib.request.Request(url,None,headers)
	response = urllib.request.urlopen(request,None,timeout=10)
	try:
		html = response.read().decode('gbk','ignore').encode('utf-8')
	except Exception as e:
		print("读取网页失败，正在尝试重新读取!")
		html = response.read().decode('gbk','ignore').encode('utf-8')

soup = BeautifulSoup(html, "html.parser")
new_soup = soup.find(name='a',attrs={"title":book_name})
try:
	catalogue_url = new_soup.get('href')
except Exception as e:
	print("该网站没有该书")
	
fileHandle = open ( book_name+'.txt', 'a',encoding='utf-8' )
print("小说目录网址："+catalogue_url)


catalogue_request = urllib.request.Request(catalogue_url,None,headers)  
catalogue_response = urllib.request.urlopen(catalogue_request,None)
catalogue_html = catalogue_response.read().decode('gbk','ignore').encode('utf-8')


catalogue_soup = BeautifulSoup(catalogue_html, "html.parser")
new_catalogue_soup = catalogue_soup.find_all('ul',class_='mulu_list')
new_catalogue_soup = new_catalogue_soup[0].find_all('a')
for item in new_catalogue_soup:
	catalogue_url_list.append(item.get('href'))

for item1 in catalogue_url_list:
	text_url = catalogue_url+item1
	try:
		text_request = urllib.request.Request(text_url,None,headers)  
		text_response = urllib.request.urlopen(text_request,None,timeout=10)
		try:
			text_html = text_response.read().decode('gbk','ignore').encode('utf-8')
		except Exception as e:
			print("读取网页失败，正在尝试重新读取!")
			text_html = text_response.read().decode('gbk','ignore').encode('utf-8')
	except Exception as e:
		print("连接请求失败，正在尝试重新连接!")
		text_request = urllib.request.Request(text_url,None,headers)  
		text_response = urllib.request.urlopen(text_request,None,timeout=10)
		try:
			text_html = text_response.read().decode('gbk','ignore').encode('utf-8')
		except Exception as e:
			print("读取网页失败，正在尝试重新读取!")
			text_html = text_response.read().decode('gbk','ignore').encode('utf-8')


	text_soup = BeautifulSoup(text_html, "html.parser")
	text_context = text_soup.find(name='div',attrs={"class":'contentbox'}).get_text('\n','br/')
	text_context = text_context[:-56]
	text_title = text_soup.find(name='div',attrs={"class":'h1title'}).h1.get_text()

	
	print("正在写入： "+ text_title)
	fileHandle.write (text_title+'\n\n'+text_context+'\n\n')

fileHandle.close()

# for item in new_catalogue_soup:
# 	item.get
# new_catalogue_soup