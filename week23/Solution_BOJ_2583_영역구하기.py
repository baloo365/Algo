import sys
sys.setrecursionlimit(10**6)

M, N, K = map(int, input().split()) # 세로, 가로
paper = [[0] * N for _ in range(M)]

def rect_area(lx, ly, rx, ry):
    height = ry - ly # 2
    width = rx - lx # 4
    for i in range(height):
        for j in range(width):
            paper[ly + i][lx + j] += 1


def dfs(a, b):
    global cnt

    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni, nj = a+di, b+dj
        if 0 <= ni < M and 0 <= nj < N and paper[ni][nj] == 0:
            paper[ni][nj] = 1
            cnt += 1
            dfs(ni, nj)

for i in range(K):
    lx, ly, rx, ry = map(int, input().split()) # 0 2 4 4
    # arr.append((lx, ly, rx, ry))
    rect_area(lx, ly, rx, ry)

# print(arr)
# print(paper)
result = 0
q = []
for i in range(M):
    for j in range(N):
        cnt = 0
        if paper[i][j] == 0:
            paper[i][j] = 1
            dfs(i, j)
            result += 1
            q.append(cnt+1)

q.sort()
print(result)
print(*q)
