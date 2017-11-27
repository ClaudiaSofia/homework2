#!/bin/python3

import sys


def timeConversion(s):
    c = s[:-2]
    h = s[:2]
    if (s[-2:] == "PM") and (h != "12"):
        n = int(h) + 12
        c = c.replace(h, str(n), 1)
    elif (s[-2:] == "AM") and (h == "12"):
        c = c.replace(h, "00", 1)

    return c


s = input().strip()
result = timeConversion(s)
print(result)