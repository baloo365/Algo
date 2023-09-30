from collections import deque
 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N개의 줄, 길이 M인 문자열
    # arr = [list(input()) for _ in range(N)] # N이 세로, M이 가로
    # print(arr)
    result = 0
    q = deque()
    visited = [[-1] * M for _ in range(N)]  # 최소거리 구하는데 0으로 두면 최소거리 구하는 데에 어려움이 있음
 
    for i in range(N):
        arr = input()
        for j in range(M):
            if arr[j] == 'W':
                q.append((i, j))    # 물의 좌표를 저장해줌.
                visited[i][j] = 0   # 물 방문 표시 해줌.
    # print(visited)
 
    # bfs()
    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            # print(ni, nj)
            if 0 <= ni <= N - 1 and 0 <= nj <= M - 1 and visited[ni][nj] == -1:  # 방문 안 한 땅을 만났을 경우
                # 방문한 경우 continue
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1  # 이전까지의 거리 누적으로 더해줌
 
 
    for i in range(N):
        for j in range(M):
            result += visited[i][j]
 
    # print(visited)
 
    print(f'#{tc} {result}')
