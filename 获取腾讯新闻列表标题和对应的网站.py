# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import requests
from bs4 import BeautifulSoup
import re


r=requests.get(url='https://new.qq.com/ch/world/')
soup=BeautifulSoup(r.text,'lxml')

path=r'/Users/weipeng/Desktop/world_index.txt'
f=open(path,'w',encoding='utf8')
f.seek(0)

f.write('2018年8月10日\n')

news=soup.find_all('a',href=re.compile('http://new.qq.com/omn/20180809'))
#通过正则，获取所有新闻的url

for i in news:
    txt=i.text.strip()   #strip（）去掉空格
    if txt=='':          #if-else去掉空行
        continue
    else:
       lst=(txt,'url=',i.attrs['href'],'\n')
       f.writelines(lst)
        
        
f.close()
print('完成')
