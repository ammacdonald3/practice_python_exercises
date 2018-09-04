# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 13:09:41 2018

@author: amacdonald1
"""

import sys

print("Let's find all of the divisors of a specific number.")
num = input("Enter a number here: ")

try:
    num = int(num)
except ValueError:
    print("You didn't enter a valid number...")
    sys.exit()


for x in range(1, num + 1):
    if num % x == 0:
        print(x)
        