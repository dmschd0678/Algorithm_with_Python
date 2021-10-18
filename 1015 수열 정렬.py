n = int(input())

A = list(map(int,input().split()))
P = sorted(A)

for i in range(n):
    print(P.index(A[i]), end = " ")
    P[P.index(A[i])] = -1