r = int(input())
ar = list(input().split(" "))


def CountingSort(l):
    cs = [0] * 100
    for e in l:
        cs[int(e)] += 1
    for i in cs:
        print(i, end=" ")


CountingSort(ar)