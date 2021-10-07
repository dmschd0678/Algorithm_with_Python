time = input().split()
time = [int(i) for i in time]

if time[1] - 45 < 0:
    time[0] -= 1
    time[1] = 60 - 45 + time[1]
else:
    time[1] -= 45

if time[0] < 0:
    time[0] = 24 + time[0]

print(time[0], time[1])