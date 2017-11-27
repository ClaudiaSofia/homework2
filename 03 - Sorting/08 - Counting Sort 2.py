r= int(input())
ar = [int(i) for i in input().strip().split()]

def count(ar):  #function of counting sort 1. It gives as result the number of times every number from 0 to 99 appears on the list.
    cs= [0]*100
    for e in ar:
        cs[e] +=1

    return (cs)
def countingsort(l):
    for e in range(100):
        for i in range(l[e]):
            print (e, end= " ")

c= count(ar)
countingsort(c)