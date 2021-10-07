num = input().split()

num[0] = num[0][::-1]
num[1] = num[1][::-1]
num = [int(i) for i in num]

print(num[0] if num[0] > num[1] else num[1])