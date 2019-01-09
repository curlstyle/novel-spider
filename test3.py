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
catalogue_url='http://www.biquyun.com/modules/article/soshu.php?searchkey=%B4%CE%D4%AA%B7%A8%B5%E4'
catalogue_request = urllib.request.Request(catalogue_url,None,headers)  
catalogue_response = urllib.request.urlopen(catalogue_request,None)
catalogue_html = catalogue_response.read()
catalogue_soup = BeautifulSoup(catalogue_html, "html.parser")
print(catalogue_soup)