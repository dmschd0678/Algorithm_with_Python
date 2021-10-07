n = input()

dic = {}

for i in range(ord('a'), ord('z') + 1):
    try:
        print(n.index(chr(i)), end = " ")
    except:
        print(-1, end= " ")