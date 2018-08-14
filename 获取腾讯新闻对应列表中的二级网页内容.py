import requests
from bs4 import BeautifulSoup
import re


r=requests.get(url='https://new.qq.com/ch/world/')
soup=BeautifulSoup(r.text,'lxml')

path=r'/Users/weipeng/Desktop/news.txt'
f=open(path,'w',encoding='utf8')
f.seek(0)

f.write('2018年8月13日\n')

news=soup.find_all('a',href=re.compile('http://new.qq.com/omn/20180813'))
#通过正则，获取所有新闻的url

for i in news:
    txt=i.text.strip()   #strip（）去掉空格
    if txt=='':          #if-else去掉空行
        continue
    else:
        u=i.attrs['href']
        print(u)
        ur=requests.get(u)
        usoup=BeautifulSoup(ur.text,'lxml')
        f.write(txt+'\n')
        f.write('正文如下：\n')
        
        p=usoup.find('div',class_='content-article').find_all('p')
        #print(p)
        #p=usoup.find_all('p')
        for i in p:
            f.write(i.text+'\n')
        
f.close()
print('完成')
