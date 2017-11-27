#!/bin/python3

import sys


n = int(input().strip())

for i in range(n):
    s = "#"*(i+1)
    print(s.rjust(n," "))