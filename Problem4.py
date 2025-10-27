#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 13:38:32 2025

@author: logan
"""

sum = 0
a = 4687
b = 9206
for i in range(a,b):
    if i % 2 == 1:
        sum += i

print(sum)