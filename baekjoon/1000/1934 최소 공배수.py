import math

n = int(input())

for i in range(n):
    l = list(map(int, input().split()))
    print(math.lcm(l[0],l[1]))