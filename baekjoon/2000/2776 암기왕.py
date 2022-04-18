import sys
from bisect import bisect_left, bisect_right

n = int(sys.stdin.readline())

for _ in range(n):
    __ = int(input())
    s1 = list(map(int, sys.stdin.readline().split()))
    __ = int(input())
    s2 = list(map(int, sys.stdin.readline().split()))
    s1.sort()
    for i in s2:
        a = bisect_left(s1, i)
        if a == len(s1):
            print(0)
        else:
            print(1)