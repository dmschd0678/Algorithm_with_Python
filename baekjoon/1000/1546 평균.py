num = int(input())

l = input().split()
l = [int(i) for i in l]

answer = []
for i in range(len(l)):
    answer.append(l[i] / max(l) * 100)

print(sum(answer) / len(answer))