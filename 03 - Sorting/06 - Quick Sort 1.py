def quickSort(l):
    pivot = l[0]
    left = []
    equal = []
    right = []
    for e in l:
        if e < pivot:
            left.append(e)
        elif e > pivot:
            right.append(e)
        else:
            equal.append(e)
    sol = left + equal + right
    sol_string = ''
    for j in range(len(sol)):
        if j == 0:
            sol_string += str(sol[j])
        else:
            sol_string += ' ' + str(sol[j])

    return sol_string


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
print(quickSort(ar))