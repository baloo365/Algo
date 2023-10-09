import sys
from collections import deque
# N * M 행렬로 표현되는 맵이 있음
# 0은 이동할 수 있고 1은 벽이라 이동 불가함
# (1, 1)에서 (N, M)으로 이동하려고 하는데 최단 경로로 이동하려고 함
# 최단 경로란 가장 적은 개수의 칸을 지나는 경로를 말함.
# 시작하는 칸과 끝나는 칸 포함함.
# 벽을 한 개까지 부수도 이동해도 됨.
# 최단 거리 출력, 불가능할 때는 -1 출력

# 구현 계획
# 델타 탐색하며 이동하는데,
# 벽을 어떻게 부수고 갈 것인가.
# 벽을 부쉈다면, 그 다음 경우의 수를 어떻게 구현할 것인가. (3차원 배열 사용하면 될 듯??)

def bfs():
    while q:
        i, j, a_break = q.popleft()

        if i == N-1 and j == M-1: # 끝점 도착했을 경우 리턴
            return visited[a_break][i][j]

        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = i + di, j + dj
            # print('nice')
            if 0 <= ni < N and 0 <= nj < M:
                # print('haha')
                if arr[ni][nj] == 1 and a_break == 1:
                    # print('hi', ni, nj)
                    visited[0][ni][nj] = visited[a_break][i][j] + 1
                    q.append((ni, nj, 0))

                elif arr[ni][nj] == 0 and visited[a_break][ni][nj] == 0:
                    # print('hello', ni, nj, a_break)
                    visited[a_break][ni][nj] = visited[a_break][i][j] + 1
                    q.append((ni, nj, a_break))

    return -1

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

# print(arr)

q = deque()
q.append((0, 0, 1)) # 시작점(i, j)와 부술 수 있는 횟수
visited = [[[0] * M for _ in range(N)] for _ in range(2)]
visited[1][0][0] = 1

print(bfs())
# print(visited)
