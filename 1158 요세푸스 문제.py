from collections import deque
n = list(map(int, input().split()))

l = deque(range(1,n[0]+1))
i = 1
print("<", end = "")
while len(l) > 1:
    if i % n[1] == 0:
        print(l.popleft(), end = ', ')
    else:
        l.append(l.popleft())
    i += 1
print(l.pop(), end=">")