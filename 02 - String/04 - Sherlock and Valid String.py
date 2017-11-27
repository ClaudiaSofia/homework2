#!/bin/python


import sys


def isValid(s):
    ele = {}
    for e in "abcdefghijklmnopqrstuvwxyz":
        times = s.count(e)
        if times > 0:
            if times in ele:
                ele[times].append(e)
            else:
                ele[times] = [e]

    if len(ele) == 2:
        keys = ele.keys()
        if (abs(keys[0] - keys[1]) == 1) and ((len(ele[keys[0]]) is 1) or (len(ele[keys[1]]) is 1)):
            return "YES"
        elif (len(ele[keys[0]]) is 1 and (keys[0] == 1)) or (len(ele[keys[1]]) is 1 and (keys[1] == 1)):
            return "YES"
        else:
            return "NO"
    elif len(ele) > 2:

        return "NO"
    else:
        return "YES"


s = raw_input().strip()
result = isValid(s)
print(result)
