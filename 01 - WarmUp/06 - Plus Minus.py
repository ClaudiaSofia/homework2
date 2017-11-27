#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
pos = 0
neg = 0
zero = 0

for e in range(n):
    if arr[e] < 0:
        neg+= 1
    elif arr[e] > 0:
        pos+= 1
    else: zero+= 1


print (float(pos/n))
print (float(neg/n))
print (float(zero/n))