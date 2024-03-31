# dp문제인데 bfs로 풀었다
# dp 알다가도 모르겠다 점화식 세우는 연습부터 해야겠다
# candy_arr가 visited 역할해줌

from collections import deque

N, M = map(int, input().split())  # N개의 줄, 총 M개의 숫자
arr = [list(map(int, input().split())) for _ in range(N)]
candy_arr = [[-1] * M for _ in range(N)]

# print(arr)

def bfs(a, b):
    q = deque()
    q.append((a, b))
    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (0, 1), (1, 1)):
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj]+candy_arr[i][j] > candy_arr[ni][nj]:
                q.append((ni, nj))
                candy_arr[ni][nj] = arr[ni][nj]+candy_arr[i][j]

candy_arr[0][0] = arr[0][0]
bfs(0, 0)
print(candy_arr[N-1][M-1])
