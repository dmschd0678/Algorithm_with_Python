import sys

N,M = list(map(int, sys.stdin.readline().split()))

l = [sys.stdin.readline().split() for _ in range(N)]

def binary(array, elem):
    s, e = 0, len(array) - 1
    result = 0
    while s <= e:
        mid = (s + e) // 2
        if int(array[mid][1]) >= elem:
            e = mid - 1
            result = mid
        else:
            s = mid + 1
    return result
for i in range(M):
    n = int(sys.stdin.readline())
    print(l[binary(l,n)][0])