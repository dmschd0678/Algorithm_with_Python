n = int(input())
c = input()

l = ""

for i in range(len(c) // n):
    if i % 2 == 0:
        l += (c[:n])
    else:
        word = c[:n]
        word = word[::-1]
        l += (word)
    c = c[n:]
print(l)
for i in range(len(l) // 2):
    for j in range(len(l) // 2):
        print(l[(j * n + i) % len(l)], end="")