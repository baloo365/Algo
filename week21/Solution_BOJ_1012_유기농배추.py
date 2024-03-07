from collections import deque

T = int(input())
# 가로 M, 세로 N, 배추가 심어져 있는 위치의 개수
# 해충 방지에 효과적인 배추 흰 지렁이 구입
# 어떤 배추에 배추 흰 지렁이가 살고 있으면
# 인접한 다른 배추로 이동 가능, 그 배추들 역시 보호 받음
# 총 몇 마리의 지렁이가 필요한지 구하시오.

def bfs(a, b):
    q = deque()
    q.append((a, b))
    while q:
        i, j = q.popleft()
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and cabbage[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni, nj))

for tc in range(T):
    M, N, K = map(int, input().split())
    cabbage = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        cabbage[y][x] = 1
    # print(cabbage)

    cnt = 0
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i, j)
                cnt += 1

    print(cnt)
