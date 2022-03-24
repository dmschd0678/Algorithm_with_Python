n = int(input())

for i in range(n):
    floor = 0
    room = 1
    guest = list(map(int, input().split()))
    while guest[2] > 0:
        floor += 1
        guest[2] -= 1
        if floor > guest[0]:
            room += 1
            floor = 1
    print("{}{:02d}".format(floor,room))

