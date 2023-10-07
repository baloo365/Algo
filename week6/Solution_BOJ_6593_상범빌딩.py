import sys
from collections import deque

# 빌딩은 1인 정육면체로 이루어져있다.
# 각 칸에서 동, 서, 남, 북, 상, 하 6개의 칸으로 1분의 시간을 들여 이동할 수 있다.
# 대각선으로 이동하는 것은 불가능하다.
# L은 층 수, R과 C는 한 층의 행과 열

def bfs():
    while q:
        z, i, j = q.popleft()

        if z == end_z and i == end_i and j == end_j:
            return visited[z][i][j]

        for dz, di, dj in ((0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1), (1, 0, 0), (-1, 0, 0)):
            nz, ni, nj = z+dz, i+di, j+dj
            if 0 <= nz < L and 0 <= ni < R and 0 <= nj < C:
                if visited[nz][ni][nj] == 0 and (arr[nz][ni][nj] == '.' or arr[nz][ni][nj] == 'E'):
                    visited[nz][ni][nj] = visited[z][i][j] + 1
                    q.append((nz, ni, nj))

    return "Trapped!"


while True:
    L, R, C = map(int, input().split())

    arr = [[] * R for _ in range(L)]
    visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]

    if L == 0 and R == 0 and C == 0:
        break

    for i in range(L):
        for _ in range(R):
            arr[i].append(list(map(str, sys.stdin.readline().strip())))
        sys.stdin.readline()

    q = deque()
    for z in range(L):
        for i in range(R):
            for j in range(C):
                if arr[z][i][j] == 'S':
                    q.append((z, i, j))
                if arr[z][i][j] == 'E':
                    end_z, end_i, end_j = z, i, j

    ans = bfs()
    # print(ans)
    if type(ans) == str:
        print(ans)
    else:
        print(f'Escaped in {ans} minute(s).')

# C개의 문자로 이루어진 R개의 행이 L번 주어진다.
# 각 문자는 한 칸을 나타낸다.
# 금으로 막혀 있어 지나갈 수 없으면 #, 비어있는 칸은 .으로 표현
# 시작 지점은 S로 표현, 탈출할 수 있는 출구는 E로 표현



