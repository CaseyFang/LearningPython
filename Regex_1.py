#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 20:55:58 2019

@author: siyuanfang
"""
name = input("Enter File Name: ")
if len(name)<1:
    name = "regex_sum_42.txt"
fhand = open(name)
total = 0
import re

for line in fhand:
    x = line.rstrip()
    y = re.findall('[0-9]+',x)
    for n in y:
        if float(n) > 0:
            total = total + float(n)
        else:
            continue
print(int(total))