N, M = list(map(int, input().split()))

l = [1 for i in range(M + 1)]

l[0] = 0
l[1] = 0

for i in range(2, int(M ** 0.5) + 1):
    if l[i]:
        j = 2
        while i * j <= M:
            l[i * j] = 0
            j += 1

for i in range(N,len(l)):
    if l[i]:
        print(i)