n = int(input())

for i in range(n):
    num = input().split()
    print(f"Case #{i + 1}:", int(num[0]) + int(num[1]))
