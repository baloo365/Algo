from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# 치즈가 모두 녹아 없어지는 데 걸리는 시작 출력
# 정사각형의 4변 중 적어도 2변 이상이 실내온도의 공기와 접촉한 것은
# 정확히 한시간만에 녹아 없어진다.
# 주어진 치즈가 모두 없어지는 시간

def inner_bfs(a, b):
    q = deque()
    visited = [[0] * M for _ in range(N)]
    q.append((a, b))
    visited[a][b] = 0
    arr[a][b] = 3
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and (arr[ni][nj] == 0 or arr[ni][nj] == 3) and visited[ni][nj] == 0:
                arr[ni][nj] = 3
                visited[ni][nj] = 1
                q.append((ni, nj))

def air_cheese(i, j):
    check = 0
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 3:
            check += 1

    return check

result = 0

while True:
    flag = True
    for row in arr:
        # print(arr)
        if 0 in row or 1 in row:
            flag = False

    if flag:
        break

    inner_bfs(0, 0)

    ch_list = []

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and air_cheese(i, j) >= 2:
                ch_list.append((i, j))

    for i in ch_list:
        arr[i[0]][i[1]] = 3

print(result)
