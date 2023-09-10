import sys
from collections import deque

# 하나의 토마토의 인접한 곳은 상하좌우 의미함
# 며칠이 지나면 보관된 토마토들이 다 익게 되는지 최소 일수 궁금쓰
# 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토 없음


def bfs():
    while q:
        i, j = q.popleft()
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0<= nj < M and tomato_arr[ni][nj] == 0 and visited[ni][nj] == -1:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj))


    return visited


M, N = map(int, input().split())
tomato_arr = [[0] for _ in range(N)]


q = deque()
visited = [[-1] * M for _ in range(N)]
check = 0

for i in range(N):
    row = list(map(int, input().split()))
    tomato_arr[i] = row
    if 0 not in row:
        check += 1

# print(check)
if check == N:
    print(0)
else:
    for i in range(N):
        for j in range(M):
            if tomato_arr[i][j] == 1:
                q.append((i, j))
                visited[i][j] = 0
            elif tomato_arr[i][j] == -1:
                visited[i][j] = 0

    bfs()
    # print(visited)
    for i in visited:
        if -1 in i:
            print(-1)
            break
    else:
        print(max(map(max, visited)))
