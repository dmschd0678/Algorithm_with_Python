tc = int(input())

for i in range(tc):
    n,m = list(map(int, input().split()))

    l = list(map(int,input().split()))
    al = [0 for i in range(n)]
    al[m] = 1
    cnt = 1
    while True:
        if max(l) == l[0]:
            if al[0] == 1:
                break
            l.pop(0)
            al.pop(0)
            cnt += 1
        else:
            l.append(l.pop(0))
            al.append(al.pop(0))
    print(cnt)

