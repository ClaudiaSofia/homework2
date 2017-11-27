#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))
st= sum(arr)

smax = st-min(arr)
smin = st-max(arr)

print (smin, smax, sep = " ")