def find_the_median(l,n):
    l.sort()
    v = int(n/2)
    return l[v]

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
print(find_the_median(ar,m))
