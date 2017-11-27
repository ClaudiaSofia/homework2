def insertionSort(l):
    new_insertion = l[-1]
    ordered_list = l[0:-1]
    last = len(ordered_list) - 1
    new_list = []
    while last >= 0:
        i = l[last]
        if i < new_insertion:
            break
        else:
            new_list = ordered_list[0:last] + [i] + ordered_list[last:]

        print(" ".join(str(s) for s in new_list))
        last = last - 1
    new_list[last + 1] = new_insertion
    print(" ".join(str(s) for s in new_list))


size = int(input())
ar = [int(i) for i in input().strip().split()]
insertionSort(ar)
