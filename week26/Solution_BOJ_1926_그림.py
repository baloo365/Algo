from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)
# 0은 색칠이 안된 부분, 1은 색칠이 된 부분
# 그림의 개수와, 그림 중 넓이가 가장 넓은 것의 넓이 출력
# 가로나 세로로 연결된 것은 연결이 된 것이고, 대각선으로 연결이 된 것은 떨어진 것

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
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                cnt += 1
                visited[ni][nj] = 1
                arr[ni][nj] = 0
                q.append((ni, nj))


max_cnt = 0
total_cnt = 0
visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        cnt = 0
        if arr[i][j] == 1:
            total_cnt += 1
            bfs(i, j)
        max_cnt = max(max_cnt, cnt)

print(total_cnt)
print(max_cnt)
