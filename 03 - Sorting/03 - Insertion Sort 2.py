def insertionSort(l):
    for i in range(1, len(l)):
        j = i - 1

        n = l[i]
        while (j >= 0) and (n < l[j]):
            l[j + 1] = l[j]
            l[j] = n
            j -= 1
        print(" ".join(str(s) for s in l))


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertionSort(ar)
