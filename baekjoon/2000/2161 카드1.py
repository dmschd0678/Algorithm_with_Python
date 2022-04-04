from collections import deque
n = int(input())

l = deque(range(1,n+1))

while len(l) > 1:
    print(l.popleft() , end = " ")
    l.append(l.popleft())

print(l.pop())