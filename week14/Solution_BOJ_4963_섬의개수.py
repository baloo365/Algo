import sys
from collections import deque

def bfs(i, j):
    dj = [1, -1, 0, 0, 1, -1, 1, -1]
    di = [0, 0, -1, 1, -1, 1, 1, -1]
    island[i][j] = 0
    q = deque()
    q.append((i, j))
    while q:
        si, sj = q.popleft()
        for i in range(8):
            nj = sj + dj[i]
            ni = si + di[i]
            # print('nice')
            if 0 <= ni < h and 0 <= nj < w and island[ni][nj] == 1:
                island[ni][nj] = 0
                q.append((ni, nj))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    island =[list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
