import sys
from collections import deque


def bfs():
    while q:
        i, j = q.popleft()
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0 and arr[i][j] == arr[ni][nj]:
                    visited[ni][nj] = 1
                    q.append([ni, nj])


def bfs2():
    while q2:
        i, j = q2.popleft()
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if arr[i][j] == 'R' or arr[i][j] == 'G':
                    if visited2[ni][nj] == 0 and (arr[ni][nj] == 'R' or arr[ni][nj] == 'G'):
                        visited2[ni][nj] = 1
                        q2.append([ni, nj])
                else:
                    if visited2[ni][nj] == 0 and arr[i][j] == arr[ni][nj]:
                        visited2[ni][nj] = 1
                        q2.append([ni, nj])


N = int(input())
# G-R차이 없음
arr = [list(input()) for _ in range(N)]

cnt = 0
q = deque()

visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            cnt += 1
            q.append([i, j])
            bfs()


cnt2 = 0
q2 = deque()
visited2 = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited2[i][j] == 0:
            cnt2 += 1
            q2.append([i, j])
            bfs2()

print(cnt, cnt2)
