# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:44:01 2019

@author: Casey.FANG
"""

lst = [0,1,2,3,4,5,6,7,8]
lstt = list()
pairs = dict()

for x in lst:
    y = 8-x
    if y in lst:
        pairs[x]=y
    else:
        continue
#print(list(pairs.items()))
temp = []
for a,b in list(pairs.items()) :
    #to check for the duplicate tuples
    if (a,b) not in temp and (b,a) not in temp: 
        temp.append((a,b))

print(temp)