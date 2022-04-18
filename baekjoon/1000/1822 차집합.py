_ = input()
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))

answer = sorted(list(s1 - s2))
print(len(answer))
print(*answer)