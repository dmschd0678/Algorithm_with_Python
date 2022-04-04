N = int(input())

apt = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14]]

for i in range(1, 14 + 1):
    floor = []
    for j in range(1, 14 + 1):
        n = 0
        for k in range(j):
            n += apt[i - 1][k]
        floor.append(n)
    apt.append(floor)

for i in range(N):
    a = int(input())
    b = int(input())
    print(apt[a][b - 1])

