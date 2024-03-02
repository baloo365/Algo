import sys
from collections import deque
import copy

# 안전 영역 크기의 최댓값을 구하라
# 빈칸 3개 골라서 1 삽입
# 바이러스는 델타 탐색하다가 1을 만나면 스톱
# 그랬을 때 0이 가장 많은 경우를 구한다.
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(temp_list):
    # print(temp_arr)
    birus_loca = deque()
    temp_arr = copy.deepcopy(temp_list)
    # 바이러스 위치 저장해준다.
    for i in range(N):
        for j in range(M):
            if temp_arr[i][j] == 2:
                birus_loca.append((i, j))

    while birus_loca:
        loca_i, loca_j = birus_loca.popleft()

        for k in range(4):   # 델타 탐색
            ni, nj = loca_i + di[k], loca_j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if temp_arr[ni][nj] == 0:
                    temp_arr[ni][nj] = 2
                    birus_loca.append((ni, nj))

    global result
    count_0 = 0

    # print(arr)
    for i in range(N):
        for j in range(M):
            if temp_arr[i][j] == 0:
                count_0 += 1

    result = max(result, count_0)

def wall(w_count):
    if w_count == 3:
        bfs(arr)
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1   # 벽 세워준다.
                wall(w_count+1)
                arr[i][j] = 0   # 원래대로 돌려줌


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = 0
wall(0)

print(result)
