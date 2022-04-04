import math

n1 = list(map(int, input().split()))

maxi = max(n1)
mini = min(n1)

print(math.gcd(maxi,mini))
print(math.lcm(maxi,mini))