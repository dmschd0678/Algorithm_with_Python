import sys

n = int(sys.stdin.readline())

stack = []

for i in range(n):
    command = sys.stdin.readline()

    if command.find("push") == 0:
        stack.append(int(command[4:-1] + command[-1]))
    if command.find("size") == 0:
        print(len(stack))
    if command.find("empty") == 0:
        print(1 if len(stack) == 0 else 0)
    try:
        if command.find("pop") == 0:
            print(stack.pop())
        if command.find("top") == 0:
            print(stack[-1])
    except:
        print(-1)
