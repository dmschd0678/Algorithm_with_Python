while True:
    l = list(map(int,input().split()))

    if l[0] + l[1] == 0: break

    if l[0] % l[1] == 0:
        print("multiple")
    elif l[1] % l[0] == 0:
        print("factor")
    else:
        print("neither")