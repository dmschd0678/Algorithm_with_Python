while True:

    try:
        num = input().split()
        num = [int(i) for i in num]
        print(num[0] + num[1])
    except:
        break