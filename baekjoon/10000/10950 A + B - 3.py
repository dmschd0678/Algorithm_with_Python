n = int(input())

l = []

for i in range(n):
    num = input().split()
    l.append(int(num[0]) + int(num[1]))
for i in l:
    print(i)