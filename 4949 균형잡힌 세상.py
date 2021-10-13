while True:

    stack = []
    str = input()

    flag = True

    if str == '.':
        break

    for i in str:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
                break


    if not stack and flag:
        print('yes')
    else:
        print('no')