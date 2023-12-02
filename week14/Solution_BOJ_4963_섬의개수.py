import sys
from collections import deque

def bfs():
    while q:
        si, sj = q.popleft()
        island[si][sj] = 0
        for di, dj in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
            ni, nj = si + di, sj + dj
            # print('nice')
            if 0 <= ni < h and 0 <= nj < w and island[ni][nj] == 1:
                island[si][sj] = 0
                q.append((ni, nj))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    island =[list(map(int, input().split())) for _ in range(h)]

    # print(w, h, island)
    visited = [[0] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                island[i][j] = 0
                q = deque()
                q.append((i, j))
                bfs()
                cnt += 1
    print(cnt)


