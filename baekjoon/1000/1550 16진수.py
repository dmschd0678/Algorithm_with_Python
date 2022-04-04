n = input()
n = n[::-1]
cnt = 0
result = 0
for i in n:
    num = 0
    if i == "A":
        num = 10
    elif i == "B":
        num = 11
    elif i == "C":
        num = 12
    elif i == "D":
        num = 13
    elif i == "E":
        num = 14
    elif i == "F":
        num = 15
    else:
        num = int(i)
    result += num * (16 ** cnt)
    cnt += 1
print(result)