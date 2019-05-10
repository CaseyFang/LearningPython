#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 22:05:08 2019

@author: siyuanfang
"""

import urllib.request, urllib.parse, urllib.error, urllib.response
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#http://py4e-data.dr-chuck.net/known_by_Meshach.html

url = input('Enter URL: ')
if len(url)<1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Meshach.html'
    
count=float(input("Enter count: "))
p = float(input("Enter position: "))-1

print("Retrieving:",url)

html = urllib.request.urlopen(url,context=ctx).read()

while count > 0 :
    soup = BeautifulSoup(html,'html.parser')
    urllst =[]
    tags = soup('a')
    for tag in tags:
        urllst.append(tag.get('href',None))
    print("Retrieving:",urllst[int(p)])
    count = count-1
    html = urllib.request.urlopen(urllst[int(p)],context=ctx).read()



