#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 11:35:48 2025

@author: logan
"""

str = "We tried list and we tried dicts also we tried Zen"
dic = {}

for word in str.split(' '):
    if word in dic:
        dic[word] += 1
    else:
        dic[word]= 1
        
for key, value in dic.items():
    print (key, value)
