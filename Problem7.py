#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 20:46:47 2025

@author: logan
"""

#Problem 7
DNA = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
dih = {}

for i in DNA:
    if i in dih:
        dih[i] += 1
    else:
        dih[i] = 1

for value, key in dih:
    print (key, value)