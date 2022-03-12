stack = []
n = int(input())
stack.append(n)

for i in range(n):
    num = int(input())

    try:
        if stack[-2] >= stack[-1]:
            stack[-1] += num
        else:
            stack.append(num)
    except:
        stack.append(num)
print(stack)


