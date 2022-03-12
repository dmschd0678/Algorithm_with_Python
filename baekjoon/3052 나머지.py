check = []

for i in range(10):
    num = int(input())
    if (num % 42) not in check:
        check.append(num % 42)
print(len(check))