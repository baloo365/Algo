def bfs():
    cnt = 0
    while q:
        i, j = q.pop(0)
        for di, dj in [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]:
            # print('hi', i, j)
            ni, nj = i + di, j + dj
            if 0 <= ni <= N-1 and 0 <= nj <= N-1 and temp[ni][nj] == 1:
                # print('hi')
                temp[ni][nj] = 0
                cnt += 1
                q.append((ni, nj))
    # print(cnt)
    return cnt


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
height = set()
ans = []

for a in area:
    for b in a:
        height.add(b)

# 비의 양에 따른 모든 경우를 다 조사
# 물에 잠기지 않는 안전한 영역의 최대 개수 출력

for rain in range(max(height)+1):
    temp = [[0] * N for _ in range(N)]
    t_lst = []
    result = []
    for i in range(N):
        for j in range(N):
            if area[i][j] > rain:
                temp[i][j] = 1  # 잠기지 않은 영역 1로 표시
                t_lst.append((i, j))    # 잠기지 않은 영역 좌표 튜플로 저장

    # print(temp, rain)

    # 잠기지 않은 영역 t_lst에 저장함.
    for i, j in t_lst:
        q = []
        q.append((i, j))
        result.append(bfs())

    area_cnt = 0
    for i in result:
        if i > 0:
            area_cnt += 1

    ans.append(area_cnt)
    # print(result)

print(max(ans))

# 빗물 높이의 경우가 안전영역에 있는 높이들만 해당하는 줄 알고 height을 2~9까지로 해서 틀렸었음
# 0부터 포함하여 안전영역 최대 높이까지를 침수 높이로 줌
