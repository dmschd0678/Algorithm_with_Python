import sys

n = int(sys.stdin.readline())

l = [int(sys.stdin.readline()) for i in range(n)]
d = {}
print(round(sum(l) / n))
print(sorted(l)[n // 2])

for i in l:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
a = []
for i,j in d.items():
    if max(d.values()) == j:
        a.append(i)
a.sort()
if len(a) == 1:
    print(a[0])
else:
    print(a[1])
print(max(l) - min(l))