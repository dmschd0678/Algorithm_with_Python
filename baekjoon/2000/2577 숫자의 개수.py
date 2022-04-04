num = 1
for i in range(3):
    num *= int(input())
num = list(str(num))
num = [int(i) for i in num]
for i in range(10):
    print(num.count(i))