import heapq

n = int(input())

hq = []
for _ in range(n):
    s = list(map(int,input().split()))

    if not hq:
        for i in s:
            heapq.heappush(hq,i)
    else:
        for i in s:
            if hq[0] < i:
                heapq.heappush(hq,i)
                heapq.heappop(hq)
print(hq[0])