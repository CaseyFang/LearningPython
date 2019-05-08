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

#http://py4e-data.dr-chuck.net/comments_211123.html

url = input('Enter - ')
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

count = 0
value = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    x=float(tag.contents[0])
    count = count+1
    value = value+x

print("Count ",int(count))
print("Sum ",int(value))
