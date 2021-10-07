num = int(input())
answer = 1
cnt = 1
while True:
    if answer >= num:
        print(cnt)
        break
    answer += 6 * cnt
    cnt += 1