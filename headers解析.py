#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 08:03:09 2018

@author: weipeng
"""

headers=input('粘贴头部信息：\n')

def header_format(h):  #用于转译网页headers信息，h用于输入headers原信息

    lst=h.split('\n')  #输出类型为list
    #print(type(lst))
    m=[]
    for i in lst:
        key=i.split(':')[0]
        value=i.split(':')[1]
        #print(key,value)
        m.append([str(key),str(value)])
    return(dict(m))
        
print("\n输出头部信息：")
print(header_format(headers))
    