n = int(input())

a = 666

for i in range(n - 1):
    while True:
        a += 1
        if str(a).find("666") != -1:
            break
print(a)