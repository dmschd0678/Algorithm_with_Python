from collections import deque
import sys

n = int(sys.stdin.readline())

deQ = deque()

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push_front":
        deQ.appendleft(command[1])

    if command[0] == "push_back":
        deQ.append(command[1])

    if command[0] == "pop_front":
        if deQ:
            print(deQ.popleft())
        else:
            print(-1)

    if command[0] == "pop_back":
        if deQ:
            print(deQ.pop())
        else:
            print(-1)

    if command[0] == "size":
        print(len(deQ))

    if command[0] == "empty":
        if deQ:
            print(0)
        else:
            print(1)

    if command[0] == "front":
        if deQ:
            print(deQ[0])
        else:
            print(-1)

    if command[0] == "back":
        if deQ:
            print(deQ[-1])
        else:
            print(-1)