import sys
from collections import deque

n = int(sys.stdin.readline())

q = deque()

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        q.append(command[1])

    if command[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())

    if command[0] == "size":
        print(len(q))

    if command[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)

    if command[0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    if command[0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])