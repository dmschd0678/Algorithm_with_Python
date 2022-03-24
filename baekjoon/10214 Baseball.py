N = int(input())

for i in range(N):
    Y = K = 0
    for j in range(9):
        y, k = map(int, input().split())
        Y += y
        K += k

    if Y > K:
        print("Yonsei")
    elif K > Y:
        print("Korea")
    elif K == Y:
        print("Draw")
