import sys
from collections import deque

n = int(sys.stdin.readline())
err_flag = False
for i in range(n):

    command = sys.stdin.readline()
    a = sys.stdin.readline()
    l = sys.stdin.readline()[1:-2].split(",")
    flag = True

    if l[0] == "":
        l = deque()
    else:
        l = deque(l)

    for j in command:
        if j == "R":
            if flag == True:
                flag = False
            else:
                flag = True
        elif j == "D":
            if len(l) == 0:
                print("error")
                err_flag = True
                break
            if flag == True:
                l.popleft()
            else:
                l.pop()
    if command.count("R") % 2 == 1:
        l.reverse()

    if not err_flag:
        print("[" + ",".join(l) +"]")
    err_flag = False