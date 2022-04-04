N = int(input())

count = 1
answer = []
stack = []

for i in range(N):
    num = int(input())

    while count <= num:
        stack.append(count)
        count += 1
        answer.append("+")
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        answer = []
        break

if answer:
    print(*answer, sep="\n")
else:
    print("NO")