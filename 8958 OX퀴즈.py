num = int(input())

l = []

for i in range(num):
    OX = input()
    for j in range(len(OX)):
        if OX[j] =='O' and j == 0:
            l.append(1)
        elif OX[j] == 'O':
            l.append(l[j - 1] + 1)
        else:
            l.append(0)
    print(sum(l))
    l = []