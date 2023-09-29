import sys
from collections import deque

def bfs():
    global cnt
    while q:
        i, j, direct = q.popleft()
        if i == N-1 and j == N-1:
            cnt += 1
            return 0

        if direct == 'r':
            for di, dj in move[0]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[ni][nj] == 0:
                        q.append((ni, nj, 'r'))

            for di, dj in move[2]: # 대각선
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[ni][nj] != 0:
                        break
                q.append((ni, nj, 'r'))


        elif direct == 'b':
            for di, dj in move[0]: # 아래
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[ni][nj] == 0:
                        q.append((ni, nj, 'r'))

            for di, dj in move[2]: # 대각선
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[ni][nj] != 0:
                        break
                q.append((ni, nj, 'r'))

        if direct == 'c':
            for di, dj in move[0]: # 오른쪽
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[ni][nj] == 0:
                        q.append((ni, nj, 'r'))

            for di, dj in move[1]: # 아래
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[ni][nj] == 0:
                        q.append((ni, nj, 'b'))

            for di, dj in move[2]: # 대각선
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[ni][nj] != 0:
                        break
                q.append((ni, nj, 'r'))

        return 1



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
move = [[(0, 1)], [(1, 0)], [(1, 0), (0, 1), (1, 1)]]

# 이동할 수 없는 경우 0을 출력
# 이동시키는 방법의 개수
# (0, 0)에서 출발해서 (n-1, n-1)에 도착
# 오른쪽, 아래, 오른쪽 아래 대각선
# 맨끝 위치가 (a, b)라고 할 때
# 오른쪽(a, b) + (0, 1)
# 아래(a, b) + (1, 0)
# 오른쪽 대각선(a, b) + (1, 0), (0, 1), (1, 1)


q = deque()
q.append((0, 0, 'r'))
bfs()
print(cnt)
