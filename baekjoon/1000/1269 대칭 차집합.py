_ = input()
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))

s = s1 & s2
s1.update(s2)
print(len(s1 - s))