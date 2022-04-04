M, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

from collections import deque

# enumerate(LIST): index, 값을 루프에서 바로 사용할 수 있게 도와줌
# A = ['a', 'b', 'c']
# for idx, char in enumerate(A):
#    idx:   0,   1,   2
#    char: 'a', 'b', 'c'

"""
- 익은 토마토는 상하좌우의 안 익은 토마토를 익게 만든다
- -1은 비어있는 칸으로, 비어있거나 대각선 토마토는 익힐 수 없다
- 이미 익은 토마토는 상하지 않는다
- (토마토가 익는데 걸리는 날짜를 계산해야한다)
- 마지막에 모든 토마토가 있었는지 확인해야한다

1. 익은 토마토의 좌표를 큐(deque)에 넣고
2. 큐에서 하나씩 좌표를 꺼내 상하좌우 토마토를 익게 만든다
3. 익힌 토마토의 좌표를 다시 큐에 넣어서 다음날 다시 2의 과정 반복
4. 더이상 큐에 좌표가 없으면, 전체 토마토 상자에서 안익은 토마토가 있는지 검사
"""

d = deque()
next_d = deque()
day = 0

# 1. 익은 토마토의 좌표를 큐(deque)에 넣고
for r, row in enumerate(A):
    """
0 0 0 0 0 0 : row, r: 0
0 0 0 0 0 0 : row, r: 1
0 0 0 0 0 0 : row, r: 2
0 0 0 0 0 1 : row, r: 3
"""
    for c, col in enumerate(row):
        """
        r: 3, row: 0 0 0 0 0 1
        c, col:
        0, 0
        1, 0
        2, 0
        3, 0
        4, 0
        5, 1
        """
        # 현재 위치가 익은 토마토라면
        # 0: 안 익은 토마토
        # -1: 빈 칸
        # 1: 익은 토마토
        if col == 1:
            d.append((r, c))  # 3, 5

# deque 안에 익은 토마토의 좌표가 들어있으니, 그 좌표 하나씩 꺼내서 사용
while d:
    r, c = d.popleft()

    # 상하좌우 토마토를 익게 만든다

    # 상하좌우의 index 값을 구하고 (-1, +1)
    # 해당 좌표가 토마토 상자 안에서 유효한지 확인
    # 그 좌표의 토마토가 안익었다면 익게 만들고
    # 새로 익은 토마토의 좌표를 큐에 추가

    """
    # 상
    if 0 <= r-1 < N and A[r-1][c] == 0:
        # 익힌다!
        A[r-1][c] = 1

        # 다음에 토마토를 익히기 위해 큐에 좌표 추가
        d.append( (r-1, c) )

    # 하

    # 좌

    # 우
    """

    """
         r  c
    상:  -1  0
    하:  +1  0
    좌:   0 -1
    우:   0 +1
    """

    for delta_r, delta_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        target_r = r + delta_r
        target_c = c + delta_c

        # (target_r, target_c): 상하좌우의 토마토 좌표

        # 범위를 벗어났을 경우에 continue
        if target_r < 0 or target_r >= N: continue
        if target_c < 0 or target_c >= M: continue

        if A[target_r][target_c] == 0:
            A[target_r][target_c] = 1
            next_d.append((target_r, target_c))
    if len(d) == 0:
        day += 1
        d = next_d
        next_d = deque()

for r, row in enumerate(A):
    for c, col in enumerate(row):
        if col == 0:
            print(-1)
            exit()

print(day - 1)