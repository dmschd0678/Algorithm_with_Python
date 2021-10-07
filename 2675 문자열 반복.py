n = int(input())

for i in range(n):
    l = input().split()
    for j in l[1]:
        print(j * int(l[0]),end="")
    print()