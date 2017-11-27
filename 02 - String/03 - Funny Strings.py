#!/bin/python3

import sys

def funnyString(s):
    t = s[::-1]
    for e in range(1,len(s)):
        if (abs(ord(s[e]) - ord(s[e-1]))) == (abs(ord(t[e]) - ord(t[e-1]))):
            continue
        else:
            return ("Not Funny")
    return ("Funny")


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)