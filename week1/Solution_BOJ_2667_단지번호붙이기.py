def bfs():
    cnt = 1
    while q:
        i, j = q.pop(0)
        visited[i][j] = 1
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = i + di, j + dj
            if 0 <= ni <= N-1 and 0 <= nj <= N-1 and map[ni][nj] == 1 and visited[ni][nj] == 0:
                # print(ni, nj)
                visited[ni][nj] = 1
                map[ni][nj] = 0
                q.append((ni, nj))
                cnt += 1

    return cnt


N = int(input())
map = [list(map(int, input())) for _ in range(N)]

q = []
visited = [[0] * (N) for _ in range(N)]

result = []
for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            q.append((i, j))
            result.append(bfs())

result.sort()
print(len(result))
for i in result:
    print(i)


