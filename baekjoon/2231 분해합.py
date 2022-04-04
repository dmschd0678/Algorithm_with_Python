n = int(input())

l = []
cp = n
while cp >= 0:
    a = cp
    for i in str(cp):
        a += int(i)
    if a == n:
        l.append(cp)
    cp -= 1

if l:
    print(min(l))
else:
    print(0)