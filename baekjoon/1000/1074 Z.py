n, r, c = map(int,input().split())

ans = 0

def function(x,y,n):
    global ans
    if x == r and y ==c:
        print(int(ans))
        exit()
    if n == 1:
        ans += 1
        return

    if not (x <= r < x + n and y <= c < y + n):
        ans += n * n
        return

    a = n / 2
    function(x,y,a)
    function(x, y + a, a)
    function(x + a, y, a)
    function(x + a, y + a, a)

function(0,0, 2 ** n)