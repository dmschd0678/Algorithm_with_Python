N,M = list(map(int, input().split()))

chess = []

result = []

for _ in range(N):
    chess.append(input())

for i in range(N - 7):
    for j in range(M - 7):
        count1 = 0
        count2 = 0

        for x in range(i, i + 8):
            for y in range(j,j + 8):
                if (x + y) % 2 == 0:
                    if chess[x][y] == "W":
                        count1 += 1
                    else:
                        count2 += 1
                else:
                    if chess[x][y] == "W":
                        count2 += 1
                    else:
                        count1 += 1
        result.append(count2)
        result.append(count1)

print(min(result))
