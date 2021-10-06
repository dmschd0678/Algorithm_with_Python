A,B,C = input().split()
A,B,C = [int(i) for i in [A,B,C]]
print(int(A / (C - B) + 1) if B < C else -1)