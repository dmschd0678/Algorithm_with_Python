M = int(input().split()[1])
l = list(map(int,input().split()))

answer = 0

for i in range(len(l)):
    for j in range(i + 1,len(l)):
        for k in range(j + 1,len(l)):
            n = l[i] + l[j] + l[k]
            if n <= M and answer < n:
                answer = n
print(answer)