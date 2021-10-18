from collections import deque

n = int(input())

deQ = deque(range(1, n + 1))

while len(deQ) > 1:
    deQ.popleft()
    deQ.append(deQ.popleft())

print(*deQ)