import sys
from collections import deque

# N * N 크기 땅이 있음
# 각각의 땅에는 나라가 하나씩 존재함.
# 인구 이동은 아래와 같음
# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상 R명 이하라면, 두나라가 공유하는 국경선을 하루 동안 연다.
# 국경선이 모두 열렸다면 인구 이동 시작
# 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 연합
# 연합을 이루고 있는 각 칸의 인구수는 연합의 인구수 / 연합을 이루고 있는 칸의 개수
# 연합을 해체하고 모든 국경선 닫음
# 인구 이동이 며칠 동안 발생하는지 구하시오

# 구현 계획
# 한 칸씩 순서대로 돌면서 인구 차이 확인한다.
# 국경선 여는 것 어떻게 표현...? visited랑 sum(연합의 인구수), cnt(몇 개인지 파악하는 용도)로 줘야 하나
# 이를 반복함 모든 경우의 차이가 L명 미만 R명 초과가 될 때까지

def bfs(a, b):
    q = deque()
    q.append((a, b))
    temp_lst = []
    temp_lst.append((a, b))
    while q:
        i, j = q.popleft()
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = i + di, j +dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if L <= abs(arr[i][j] - arr[ni][nj]) <= R:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
                    temp_lst.append((ni, nj))

    return temp_lst


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
while True:
    temp_check = False
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                result_lst = bfs(i, j)
                if len(result_lst) > 1:
                    temp_check = True
                    temp_sum = 0
                    for a, b in result_lst:
                        temp_sum += arr[a][b]
                    temp_avg = temp_sum // len(result_lst)

                    for y, x in result_lst:
                        arr[y][x] = temp_avg

    if temp_check == False:
        break

    ans += 1

print(ans)
