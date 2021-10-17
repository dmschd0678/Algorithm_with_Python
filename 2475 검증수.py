l = list(map(int, input().split()))

chknum = 0

for i in l:
    chknum += i ** 2
print(chknum % 10)