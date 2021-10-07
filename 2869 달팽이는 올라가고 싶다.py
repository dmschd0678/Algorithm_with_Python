A, B, V = map(int, input().split(" "))

# l = 0
day = 0
# while True:
#        l += A
#        day += 1
#        if l >= V:
#            break
#        l -= B

day = (V - B) / (A - B)

print(int(day) if day == int(day) else int(day) + 1)