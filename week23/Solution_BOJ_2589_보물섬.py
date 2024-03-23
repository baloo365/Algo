# 트리의 지름 개념을 이용하면 답을 구할 수 있지 않을까 생각해봤으나,
# 7 7
# WLLLLLW
# LWLWLWW
# LLLWLWW
# LWWWLWW
# LLLLLWW
# LWWWWWW
# WWWWWWW
# 위의 경우처럼 트리 형태가 아닐 수도 있기 때문에 트리 지름으로는 풀 수 없다.

# 이차원 배열에서 최대값을 구하는 컴프리헨션이다.
# map을 안 써서 계속 틀렸었음.
# max(map(max, 배열))

# bfs에서 visited 배열을 안에 넣는 경우가 있고, 밖에 빼놓는 경우가 있는데,
# 문제에 따라 이부분을 잘 고려해야 할 것 같다.

from collections import deque

sero, garo = map(int, input().strip().split())
treasure = [list(input().strip()) for _ in range(sero)]
# print(treasure)
# 보물은 가장 긴 시간이 걸리는 육지 두곳에 나뉘어 묻혀있음
# 각 W에서 bfs를 도는데 가장 오래 걸리는 거 구하면 될 듯


def bfs(a, b):
    visited = [[0] * garo for _ in range(sero)]
    q = deque()
    q.append((a, b))
    visited[a][b] = 1
    while q:
        ai, bj = q.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = ai+di, bj+dj
            if 0 <= ni < sero and 0 <= nj < garo and treasure[ni][nj] == 'L' and visited[ni][nj] == 0:
                visited[ni][nj] = visited[ai][bj] + 1
                q.append((ni, nj))

    return max(map(max, visited))-1


max_result = 0
for i in range(sero):
    for j in range(garo):
        if treasure[i][j] == 'W':
            continue
        else:
            temp_result = bfs(i, j)
            # print(visited)
        # print(max([a for a in visited]))
        max_result = max(max_result, temp_result)

print(max_result)
