n = int(input())
d = {}
for i in range(n):
    x, s = input().strip().split()
    xi = int(x)

    if i < n / 2:
        s = "-"
    if xi in d:
        d[xi].append(s)
    else:
        d[xi] = [s]
for e in d:
    for i in range(len(d[e])):
        print(d[e][i], end=" ")