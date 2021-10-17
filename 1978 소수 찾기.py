import math

def prime(num):
    for j in range(2,int(math.sqrt(num)) + 1):
        while num % j == 0:
            return False
    return True

n = input()
l = list(map(int, input().split()))

cnt = 0

for i in l:
    if prime(i) and i != 1:
        cnt += 1
print(cnt)

