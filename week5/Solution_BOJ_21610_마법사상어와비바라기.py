import sys
from collections import deque

N, M = map(int, input().split())
# 바구니에 저장되어 있는 물의 양
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)

# 방향 1~8
direction = ((0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
# 대각선 방향
cross = ((-1, 1), (1, 1), (1, -1), (-1, -1))
# q에 (N, 1), (N, 2), (N-1, 1), (N-1, 2)를 담는다.
queue = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
queue = deque(queue)

for _ in range(M):
    visited = [[0] * N for _ in range(N)]
    d, s = map(int, input().split())
    di, dj = direction[d]

    new_arr_lst = []
    for idx in range(len(queue)):
        i, j = queue[idx]

        ni, nj = (i + s * di)%N, (j + s * dj)%N
        # print(i, j, 'ni', ni, 'nj', nj, d, s, di, dj)

        # 1을 더해준다.
        arr[ni][nj] += 1
        # 방문 표시를 해준다.
        visited[ni][nj] = 1
        # 대각선을 살펴보고 더해준다.
        new_arr_lst.append((ni, nj))
        # print(new_arr_lst)

    for arr_lst in new_arr_lst:
        p, q = arr_lst[0], arr_lst[1]
        # print('hi', p, q)
        for a, b in cross:
            ni2, nj2 = a + p, b + q
            if 0 <= ni2 < N and 0 <= nj2 < N:
                if arr[ni2][nj2] > 0:
                    arr[p][q] += 1

    queue = []
    # arr_lst를 제외한 나머지 칸 중에서 물의 양이 2이상인 칸의 물이 2만큼 줄어든다.
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0 and arr[r][c] >= 2:
                arr[r][c] -= 2
                # visited 원래대로 돌려줌
                # visited[i][j] = 1
                queue.append((r, c))
                # print(queue)


# print(arr)
print(sum(map(sum, arr)))
