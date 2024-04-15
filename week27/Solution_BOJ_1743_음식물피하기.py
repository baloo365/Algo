from collections import deque

N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

# print(arr)
# 제일 큰 음식물의 크기를 구해라.

def bfs(a, b):
    global cnt
    global visited
    arr[a][b] = 0
    cnt += 1
    visited[a][b] = 1
    q = deque()
    q.append((a, b))
    while q:
        start_i, start_j = q.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = start_i + di, start_j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                cnt += 1
                visited[ni][nj] = 1
                arr[ni][nj] = 0
                q.append((ni, nj))


max_cnt = 0
total_cnt = 0
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        cnt = 0
        if arr[i][j] == 1:
            total_cnt += 1
            bfs(i, j)
        max_cnt = max(max_cnt, cnt)

print(max_cnt)
