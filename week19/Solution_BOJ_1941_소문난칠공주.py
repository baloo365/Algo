arr = [list(input()) for _ in range(5)]
total_cnt = 0

def dfs(i, j, y_cnt, p_cnt, visited):
    global total_cnt

    # 이다솜파가 4명 이상이어야 함으로 반대로 임도연파가 4명 이상일 경우 종료
    if y_cnt >= 4 or p_cnt > 7:
        return

    # 7명이 찼을 경우에 경우의 수 1 추가
    if p_cnt == 7 and y_cnt < 4:
        total_cnt += 1
        return

    for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ni, nj = i+di, j+dj
        if 0 <= ni < 5 and 0 <= nj < 5 and not visited[ni][nj]:
            visited[ni][nj] = 1
            if arr[ni][nj] == 'Y':
                dfs(ni, nj, y_cnt + 1, p_cnt + 1, visited)
                visited[ni][nj] = 0
            else:
                dfs(ni, nj, y_cnt, p_cnt + 1, visited)
                visited[ni][nj] = 0

for i in range(5):
    for j in range(5):
        visited = [[0] * 5 for _ in range(5)]
        visited[i][j] = 1
        if arr[i][j] == 'Y':
            dfs(i, j, 1, 1, visited)
        else:
            dfs(i, j, 0, 1, visited)

print(total_cnt)
