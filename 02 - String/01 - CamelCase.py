#!/bin/python3

import sys


s = input().strip()
n =1
for e in range(len(s)):
    if s[e].isupper():
        n+=1
print (n)