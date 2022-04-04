import sys

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,1,0,1,-1,-1,1,0]

sys.setrecursionlimit(99999)

def dfs(x,y):
    for i in range(len(dx)):
        if 0 <= x < h and 0 <= y < w:
            if l[x][y] == 1:
                l[x][y] = 2
                for i in range(len(dx)):
                    dfs(x + dx[i], y + dy[i])

while True:
    w,h = list(map(int,input().split()))

    if w == h == 0:
        break

    l = []

    for _ in range(h):
        l.append(list(map(int,input().split())))

    cnt = 0
    for i in range(h):
        for j in range(w):
           if l[i][j] == 1:
               cnt += 1
               dfs(i,j)
    print(cnt)