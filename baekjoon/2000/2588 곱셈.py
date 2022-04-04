num = int(input())
num2 = input()

for i in range(len(num2)):
    print(num * int(num2[len(num2) - i - 1]))

print(num * int(num2))