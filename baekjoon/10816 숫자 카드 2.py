import sys

size = 20000000

arr = [0] * 20000001

_ = sys.stdin.readline()

n = list(map(int,sys.stdin.readline().split()))

for i in n:
    arr[size // 2 + i] += 1

sys.stdin.readline()

m = list(map(int,sys.stdin.readline().split()))

for j in m:
    print(arr[size // 2 + j], end = " ")