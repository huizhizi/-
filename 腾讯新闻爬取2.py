#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 08:21:08 2018

@author: weipeng
"""

import requests
from bs4 import BeautifulSoup
import re


def url_analysis(u,h,s):
    '''
    用于分析网页，最后得到一个含有二级网址的标签列表
    u：起始网址
    h：头部信息
    s：二级网址包含特定字段
    '''
    r=requests.get(url=u,headers=h)
    soup=BeautifulSoup(r.text,'lxml')
    news=soup.find_all('a',href=re.compile(s))   #查找包含s字段的网页标签
    return(news)   #返回包含二级网址的列表
    

def content(new,h):
    '''
    用于抓取网页中的标题以及新闻内容
    new：含有二级网址链接的标签
    h：头部信息
    '''
    t=new.text.strip()  #获取新闻标题
    u2=new.attrs['href']  #获取新闻链接
    
    r2=requests.get(url=u2,headers=h)
    soup2=BeautifulSoup(r2.text,'lxml')
    #p=soup2.find('div',class_='content-article').find_all('p')
    p=soup2.find_all('p')
    
    p_lst=[]
    for i in p:
        p_lst.append(i.text)
    p2='\n'.join(p_lst)
    return([t,p2])
    
    
def write_txt(name,path,content_dic):
    '''
    用于把爬取数据写入文档txt
    name：新建文档名字
    path：路径
    content_dic：需要写入的数据，字典
    '''
    f=open(path+name,'w')
    f.seek(0)
    f.write('腾讯新闻\n\n\n')
    for i in content_dic:
        f.write(i+'\n')  #写入字典的key，也就是新闻标题
        f.write(content_dic[i])  #写入字典的value，也就是新闻正文
        f.write('\n')
    f.close()
    
if __name__=='__main__':    #main函数
    web_u='https://new.qq.com/ch/world/'
    web_h={
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'accept-encoding': 'gzip, deflate, br', 
           'accept-language': 'zh-CN,zh;q=0.9', 
           'cache-control': 'max-age=0', 
           'cookie': 'pgv_pvi=7150579712; RK=EJX7jkb+da; pac_uid=1_402170612; tvfe_boss_uuid=c44b92fd7bd85bd3; mobileUV=1_15b794cf5d3_6dcf6; ptcz=80711c459e2f87b443d5172cb4972c4d8d2f431cf2b61238b2f8d4c171b21891; pgv_pvid=8605699906; AMCV_A8023A875666943A7F000101%40AdobeOrg=1406116232%7CMCIDTS%7C17618%7CMCMID%7C64243502897573354010901948445788190558%7CMCAAMLH-1522736424%7C11%7CMCAAMB-1522736424%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1522138824s%7CNONE%7CMCSYNCSOP%7C411-17625%7CMCAID%7CNONE%7CvVersion%7C2.5.0; pt2gguin=o0402170612; o_cookie=402170612; gaduid=5b1f23af56ba7; _ga=GA1.2.1836882538.1529994214; ts_refer=news.qq.com/; ts_uid=9519644743; pgv_info=ssid=s3958177168; pgv_si=s8287783936; dm_login_weixin_rem=; qm_authimgs_id=0; qm_verifyimagesession=h0187613ca885c8d436c063986b2e0931e125c56514399b4668a9b5ebdd26edbc4e628b7663a34b74fa; logout_page=dm_loginpage; dm_login_weixin_scan=; qm_ftn_key=57bf5b04; ts_last=new.qq.com/ch/world/; ad_play_index=84', 
           'referer': 'http', 
           'upgrade-insecure-requests': '1', 
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
           }
    web_s='http://new.qq.com/omn/20180821/'
    path=r'/Users/weipeng/Desktop/'
    
    m=[]
    for i in url_analysis(web_u,web_h,web_s):
        m.append(content(i,web_h))
    result=dict(m)
    write_txt('news.txt',path,result)
    print('完成')

