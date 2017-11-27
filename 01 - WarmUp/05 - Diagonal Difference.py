#!/bin/python3

import sys


n = int(input().strip())
a = []
r = 0
l= 0

for i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
    r+= int(a_t[i])
    l+= int(a_t[-(i+1)])

print (abs(r-l))