#!/bin/python3

import sys


def sherlockAndAnagrams(s):
    a = 0
    d = {}
    for i in range(len(s)):
        for j in range(len(s) - i):
            s1 = ''.join(sorted(s[j:j + i + 1]))
            d[s1] = d.get(s1, 0) + 1
    for key in d:
        a += (d[key] - 1) * d[key] // 2
    return a


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = sherlockAndAnagrams(s)

    print(result)