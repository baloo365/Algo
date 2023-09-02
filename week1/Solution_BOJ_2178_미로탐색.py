N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, input())) for _ in range(N)]
# print(maze)

q = [(0, 0)]
maze[0][0] = 2

def bfs():
    global cnt
    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            # print('hi')
            if 0 <= ni <= N-1 and 0 <= nj <= M-1 and maze[ni][nj] == 1 and (ni, nj != N-1, M-1):
                # print('hi', ni, nj)
                maze[ni][nj] = maze[i][j] + 1
                q.append((ni, nj))

            # elif 0 <= ni <= N-1 and 0 <= nj <= M-1 and ni == N-1 and nj == M-1:
              #  break

bfs()
print(maze[N-1][M-1] -1)
