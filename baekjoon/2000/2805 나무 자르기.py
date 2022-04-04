n, m = list(map(int, input().split()))
l = list(map(int, input().split()))

start = 0
end = max(l)

while start <= end:
    mid = (start + end) // 2

    c = [i - mid for i in l if i - mid > 0]
    if sum(c) >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)