while True:
    num = input().split()
    num = [int(i) for i in num]

    if num[0] == 0 and num[1] == 0:
        break
    print(num[0] + num[1])