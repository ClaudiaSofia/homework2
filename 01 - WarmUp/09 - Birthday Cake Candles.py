#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    l= []
    ma= max(ar)
    for e in range(n):
        if ar[e]== ma:
            l.append(ar[e])
    return (len(l))

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
