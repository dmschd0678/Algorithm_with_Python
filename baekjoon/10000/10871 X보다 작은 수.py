n = input().split()
print(" ".join(str(i) for i in (j for j in input().split() if int(j) < int(n[1]))))
