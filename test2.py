import urllib
from bs4 import BeautifulSoup
from xlwt import *  
import random

book_name=""
book_num=""

book_name = input("请输入书名:")

book_name1 = urllib.parse.quote(book_name.encode('gb2312'))
url = "http://www.biquyun.com/modules/article/soshu.php?searchkey="+book_name1
fileHandle = open ( book_name+'.txt', 'a',encoding='utf-8' )
print(url)
headers = {'Accept': '*/*',
           'Accept-Language': 'en-US,en;q=0.8',
           'Cache-Control': 'max-age=0',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
           'Connection': 'keep-alive',
           'Referer': 'http://www.biquge.com.tw/'
           }
# proxy = {'http':''}       
# proxy_support = urllib.request.ProxyHandler(proxy)
# opener = urllib.request.build_opener(proxy_support)
# urllib.request.install_opener(opener)
def getCatalogueList(book_url):
	catalogue_url_list = []
	catalogue_url=book_url
	catalogue_request = urllib.request.Request(catalogue_url,None,headers)  
	catalogue_response = urllib.request.urlopen(catalogue_request,None)
	catalogue_html = catalogue_response.read().decode('gbk','ignore')
	catalogue_soup = BeautifulSoup(catalogue_html, "html.parser")
	catalogue_list = catalogue_soup.find(name='div',attrs={"id":'list'}).find_all('a')
	for item in catalogue_list:
		catalogue_url_list.append(item.get('href'))
	return catalogue_url_list

def write_novel(text_url):
	try:
		text_request = urllib.request.Request(text_url,None,headers)  
		text_response = urllib.request.urlopen(text_request,None,timeout=10)
		try:
			text_html = text_response.read().decode('gbk','ignore')
		except Exception as e:
			print("读取网页失败，正在尝试重新读取!")
			text_html = text_response.read().decode('gbk','ignore')
	except Exception as e:
		print("连接请求失败，正在尝试重新连接!")
		text_request = urllib.request.Request(text_url,None,headers)  
		text_response = urllib.request.urlopen(text_request,None,timeout=10)
		try:
			text_html = text_response.read().decode('gbk','ignore')
		except Exception as e:
			print("读取网页失败，正在尝试重新读取!")
			text_html = text_response.read().decode('gbk','ignore')

	text_soup = BeautifulSoup(text_html, "html.parser")
	if text_soup!=None:
		text_context = text_soup.find(name='div',attrs={"id":'content'}).get_text('\n','br/')
		if text_context!=None:
			text_title = text_soup.h1.get_text()
			if text_title!=None:
				print("正在写入： "+ text_title)
				fileHandle.write (text_title+'\n\n'+text_context+'\n\n')

	#fileHandle.close()

if __name__ == '__main__':
	catalogue_url_list=[]
	try:
		request = urllib.request.Request(url,None,headers)
		response = urllib.request.urlopen(request,None,timeout=10)
		try:
			html = response.read()
		except Exception as e:
			print("读取网页失败，正在尝试重新读取!")
			html = response.read()
	except Exception as e:
		print("连接请求失败，正在尝试重新连接!")
		request = urllib.request.Request(url,None,headers)
		response = urllib.request.urlopen(request,None,timeout=10)
		try:
			html = response.read()
		except Exception as e:
			print("读取网页失败，正在尝试重新读取!")
			html = response.read()
	
	soup = BeautifulSoup(html, "html.parser")
	
	td_soup = soup.find_all(name='td',attrs={"class":'odd'})

	if td_soup==[]:
		div_soup = soup.find(name='div',attrs={"class":'box_con'})
		if div_soup!=None:
			catalogue_list = soup.find(name='div',attrs={"id":'list'}).find_all('a')
			for item in catalogue_list:
				catalogue_url_list.append(item.get('href'))

			for item in catalogue_url_list:
				item_url = 'http://www.biquge.com.tw'+item
				write_novel(item_url)
			fileHandle.close()
		else:
			print(div_soup)
	else:
		s_book_name = []
		s_book_writer = []
		no =[]
		for x in range(0,len(td_soup),3):
			s_book_name.append(td_soup[x].string)
			s_book_writer.append(td_soup[x+1].string)
		print(s_book_name)
		print(s_book_writer)

		for x in range(0,len(s_book_name)):
			no.append(x)
			print(str(x)+'.书名：'+s_book_name[x]+'        作者：'+s_book_writer[x])
		print(no)
		book_no = input("请输入小说序号：")
		while int(book_no) not in no:
			print('请输入正确的序号')
			book_no = input("请输入小说序号：")
		book_url = td_soup[int(book_no)*3].find('a').get('href')
		catalogue_url_list = getCatalogueList(book_url)
		for item in catalogue_url_list:
			item_url = 'http://www.biquge.com.tw'+item
			write_novel(item_url)
		fileHandle.close()




