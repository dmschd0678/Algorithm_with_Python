import copy

n = int(input())

for i in range(n):
    ps = list(input())
    cp = []
    for j in ps:
        try:
            if j == ')':
                cp.pop()
            else:
                cp.append(j)
        except Exception:
            cp.append(")")
            break
    if len(cp) == 0:
        print("YES")
    else:
        print("NO")
