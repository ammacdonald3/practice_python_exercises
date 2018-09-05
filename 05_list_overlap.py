#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 20:49:04 2018

@author: andrewmacdonald
"""

l1 = [1, 2, 3, 4, 5, 7, 2, 1, 9, 2, 6]
l2 = [2, 4, 6, 8, 10, 5, 1]

        
print(list(set([x for x in l1 if x in l2])))
