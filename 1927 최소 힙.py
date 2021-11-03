import sys
import heapq

n = int(sys.stdin.readline())

hq = []

for _ in range(n):
    value = int(sys.stdin.readline())

    if value == 0:
        try:
            print(heapq.heappop(hq))
        except:
            print(0)
    else:
        heapq.heappush(hq,value)