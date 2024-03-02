N, E_p, W_p, S_p, N_p = map(int, input().split())

# 통제할 수 없는 미친 로봇이 평면 위에 있다.
# N번의 행동을 취한다.
# 로봇은 4개의 방향 중에 하나를 임의로 선택하고 그 방향으로 이동
# 로봇이 같은 곳을 한번보다 많이 이동하지 않을 떄, 로봇의 이동 경로 단순
# 로봇이 시작하는 위치가 처음 방문한 곳
# 로봇의 이동 경로가 단순할 확률을 구하시오.
# N은 14보다 작거나 같은 자연수
visited = [[0] * 29 for _ in range(29)]
# 로봇 출발점을 (14, 14)라고 하자

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
# 0일 때: 동, 1일 때: 서, 2일 때, 남, 3일 때: 북
percent = [E_p, W_p, S_p, N_p]
answer = 0
visited[14][14] = 1

def dfs(i, j, cnt, result):
    global answer

    if cnt == N:
        # print(result*((0.01)**N))
        answer += result
        return

    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < 29 and 0 <= nj < 29 and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            dfs(ni, nj, cnt+1, result*percent[k]*0.01)
            visited[ni][nj] = 0

dfs(14, 14, 0, 1)
print(answer)
