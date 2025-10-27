#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 16:18:16 2025

@author: logan
"""

#Problem 5

inputfile = open ("input.txt", "r")
newfile = open("output.txt", "w")

for i, line in enumerate(inputfile):
    if i % 2 == 1:
        newfile.write(line)


inputfile.close()
newfile.close()