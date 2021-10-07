stick = input()
stack = []
check = False
cnt = 0

for i in stick:
    if i == '(':
        stack.append(i)
        check = True
    else:
        stack.pop()
        if (check == True):
            cnt += len(stack)
        else:
            cnt += 1
        check = False
print(cnt)
