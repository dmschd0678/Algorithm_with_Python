import sys

n = int(sys.stdin.readline())

xy = []

for _ in range(n):
    xy.append(list(map(int,sys.stdin.readline().split())))

xy.sort(key = lambda x:(x[1], x[0]))

for x,y in xy:
    print(x,y)