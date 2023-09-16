import sys
from collections import deque


# 비어있는 곳은 .
# 물이 차 있는 지역은 *
# 돌은 x
# 비버 굴은 D
# 고슴도치 위치는 S

R, C = map(int, input().split())
map = [list(input()) for _ in range(R)]
q = deque()
water_lst = set()

for i in range(R):
    for j in range(C):
        if map[i][j] == 'D':
            beaver = (i, j)
        elif map[i][j] == 'S':
            dochi = (i, j)
        elif map[i][j] == '*':
            water_lst.add((i, j))

q.append((dochi[0], dochi[1], water_lst))
cnt = 0

while q:
    dochi_i, dochi_j, water_lst = q.popleft()

    if dochi_i == beaver[0] and dochi_j == beaver[1]:
        print(cnt)

    temp_lst = set()
    for water_i, water_j in water_lst:
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            water_ni, water_nj = water_i + di, water_j + dj
            if 0 <= water_ni < R and 0 <= water_nj < C:
                if map[water_ni][water_nj] == '.':
                    map[water_ni][water_nj] = '*'
                    temp_lst.add((water_ni, water_nj))
                else:
                    continue

    q.append(temp_lst)

    dochi_i, dochi_j = dochi
    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        dochi_ni, dochi_nj = water_i + di, water_j + dj
        if 0 <= dochi_ni < R and 0 <= dochi_nj < C:
            if map[dochi_ni][dochi_nj] == '.':
                q.append((dochi_ni, dochi_nj))
                cnt += 1


