# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:54:54 2019

@author: Casey.FANG
"""


x =input("请问哥哥想看宝贝的第几种秀? 输入1-20: ")
file =open("baby20show.txt")
lst = list()

#number input
if float(x)>0 and float(x)<=20:
    x=float(x)
else:
    x=input("臭哥哥！输入1-20任意数字: ")
    x=float(x)
n=int(x)
#print(n)

#file to list
for line in file:
    line=line.rstrip()
    y=line.split("\n")
    #print(y)
    for i in y:
    	if not i in lst:
            lst.append(i)
            
print(lst[n])