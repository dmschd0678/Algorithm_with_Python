from collections import deque

n, m = map(int,input().split())
q = deque(range(1, n + 1))
l = deque(map(int, input().split()))
cnt = 0

while l:
    mid = len(q) // 2
    if q.index(l[0]) > mid:
        while q[0] != l[0]:
            q.appendleft(q.pop())
            cnt +=1
        q.popleft()
        l.popleft()
    else:
        while q[0] != l[0]:
            q.append(q.popleft())
            cnt+=1
        q.popleft()
        l.popleft()
print(cnt)