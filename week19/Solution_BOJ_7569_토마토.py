from collections import deque


# M은 상자 가로 칸, N은 상자 세로 칸, H는 높이
M, N, H = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# print(arr)

# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
deq = deque()
def bfs():
    while deq:
        i, j, z = deq.popleft()
        for di, dj, dz in ((0, 1, 0), (0, -1, 0), (-1, 0, 0), (1, 0, 0), (0, 0, -1), (0, 0, 1)):
            ni, nj, nz = i+di, j+dj, z+dz
            if 0 <= ni < N and 0 <= nj < M and 0 <= nz < H:
                if arr[nz][ni][nj] == 0 and visited[nz][ni][nj] == 0:
                    deq.append((ni, nj, nz))
                    arr[nz][ni][nj] = arr[z][i][j] + 1
                    visited[nz][ni][nj] = 1

visited = [[[0] * M for _ in range(N)] for _ in range(H)]
cnt = 0

for z in range(H):
    for i in range(N):
        for j in range(M):
            if arr[z][i][j] == 1 and visited[z][i][j] == 0:
                deq.append((i, j, z))
                visited[z][i][j] = 1
bfs()

temp = False
for z in range(H):
    for i in range(N):
        for j in range(M):
            if arr[z][i][j] == 0:
                temp = True
if temp:
    print(-1)
else:
    max_result = 0
    for z in range(H):
        for i in range(N):
            for j in range(M):
                max_result = max(max_result, arr[z][i][j])
    print(max_result -1)
