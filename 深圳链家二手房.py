#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 08:28:15 2018

@author: weipeng
"""

import requests
from bs4 import BeautifulSoup
import re


def url_analysis(u,h,s,n):
    '''
    用于分析网页，最后得到一个含有二级网址的标签列表
    u：起始网址
    h：头部信息
    s：二级网址包含特定字段
    n：页码
    '''
    
    url_lst=[]
    for i in range(1,n+1):
        r=requests.get(url=u+str(i)+'/',headers=h)
        r.encoding='utf-8'
        soup=BeautifulSoup(r.text,'lxml')
        r2=soup.find_all('a',href=re.compile(s))   #查找包含s字段的网页标签
        
        for j in r2[1::2]:
            r3=j.attrs['href']
            #r3=j.text
            url_lst.append(r3)
        
    return(url_lst)
    
    
def  content(u,h):
    '''爬取网页标签信息
    u：爬取的二级网址
    h：头部信息
    '''
    r=requests.get(url=u,headers=h)
    r.encoding='utf-8'
    soup=BeautifulSoup(r.text,'lxml')
    t=soup.title.text  #爬取标题
    toprice=soup.find('div',class_='price').find('span',class_='total').text
    #爬取总价
    unprice=soup.find('div',class_='unitPrice').find('span',class_='unitPriceValue').text[:-4]
    #爬取单价
    area=soup.find('div',class_="mainInfo").text
    #爬取面积
    base=soup.find('div',class_="base").find('div',class_="content").find_all('li')    
    year=base[-1].text[-3:-1]
    #爬取产权年限
    pattern='resblockPosition:\'(.*?)\',\n'  #正则表达式
    position=re.search(pattern,r.text).group(1)    #提取经度和维度坐标，由于是字符串所以需要将中间的','分隔
    lng=position.split(',')[0]
    lat=position.split(',')[1]    
    return([t,',',toprice,',',unprice,',',area,',',year,lng,',',lat,',','\n'])
    
    
def write_txt(path,content):
    '''
    用于把爬取数据写入文档txt
    path：新建文档名字
    content：需要写入的数据
    '''
   
    f.writelines(content)  #写入字典的value，也就是新闻正文
    f.write('\n')
  
           

if __name__=='__main__':    #main函数
    web_u='https://sz.lianjia.com/ershoufang/pg'
    web_h={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'Accept-Encoding': 'gzip, deflate, br', 
           'Accept-Language': 'zh-CN,zh;q=0.9', 
           'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 
           'Cookie': 'lianjia_uuid=61a90944-72c0-43f2-9a24-455356eb0a3d; _smt_uid=5b5fa971.458db779; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1532995954; UM_distinctid=164edade65cabd-09bf5d95f8c946-163b6950-1fa400-164edade65d217; _jzqa=1.1606693433712820700.1532995955.1532995955.1532995955.1; _jzqx=1.1532995955.1532995955.1.jzqsr=google%2Ecom%2Ehk|jzqct=/.-; _ga=GA1.2.1818159121.1532995958; select_city=440300; all-lj=27f330b89ebf795db1cd23e4c626cb3b; lianjia_ssid=23e6cf24-23fa-4d92-8812-ec4afa540edd; TY_SESSION_ID=d105d55c-cb43-4649-9b5d-1ba5aed74b16', 
           'Host': 'sz.lianjia.com', 
           'Upgrade-Insecure-Requests': '1', 
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
           }
    web_s='https://sz.lianjia.com/ershoufang/105'
    path=r'/Users/weipeng/Desktop/链家二手房.txt'
    f=open(path,'w')
    for i in url_analysis(web_u,web_h,web_s,1):
        data=content(i,web_h)
        print(data)
        write_txt(path,data)
    f.close()
    print('爬取完成！')
    
    
    
 
