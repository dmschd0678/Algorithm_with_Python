l = []

while True:
    try:
        l.append(int(input()))
    except:
        break
print(max(l))
print(l.index(max(l)) + 1)