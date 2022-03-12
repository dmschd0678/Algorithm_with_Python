num = set(range(1, 10001))
num2 = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    num2.add(i)

num = sorted(num - num2)

for i in num:
    print(i)