import math

n,m = list(map(int, input().split()))

print(math.factorial(n) // (math.factorial(m) * math.factorial(n - m)))