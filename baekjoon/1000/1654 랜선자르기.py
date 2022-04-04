N, K = list(map(int, input().split()))

l = [int(input()) for i in range(N)]
cm = sum(l) // len(l)

# while cm > 0:
#     answer = 0
#     answer += sum([i // cm for i in l])
#     if answer >= K:
#         print(cm)
#         break
#     cm -= 1

start, end = 1 , max(l)

while start <= end:
    mid = (start + end) // 2
    a = 0
    for i in l:
        a += i // mid
    if a >= K:
        start = mid + 1
    else:
        end = mid - 1

print(end)
