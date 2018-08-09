# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import requests
from bs4 import BeautifulSoup

r=requests.get(url='https://new.qq.com/omn/20180809/20180809A06OIG.html')
headers=r.headers   
#获取url的头部信息
soup=BeautifulSoup(r.text,'lxml')
title=soup.title.text
#获取title内容

path=r'/Users/weipeng/Desktop/headers.txt'
f=open(path,'w',encoding='utf8')
f.seek(0)
f.write('爬取网页：https://new.qq.com/omn/20180809/20180809A06OIG.html\n')
f.write('新闻标题：'+title+'\n')



for i in headers:
    lst=[i,':',headers[i],'\n']
    f.writelines(lst)
#headers为字典类型，因此用for循环进行遍历输出

f.close()
print('完成')