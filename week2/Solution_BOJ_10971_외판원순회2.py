def dfs(cnt):
    global min_sum
    if cnt == N:    # 순열이 완성되었을 때
        tmp = path + [path[0]]  # 다시 원래 도시로 돌아와야 함으로 원래 도시를 리스트에 더해줌
        tmp_sum = 0
        ans = 1
        for a in range(N):
            if cost[tmp[a]-1][tmp[a+1]-1] == 0:    # 갈 수 없는 도시로 가는 경우가 포함될 경우 제외(ans = 0으로 표시해줌)
                ans = 0
                break
            tmp_sum += cost[tmp[a]-1][tmp[a+1]-1]   # cost배열과 인덱스 맞게 해주려고 -1 해줌
            if tmp_sum > min_sum:   # 시간을 줄이기 위한 백트래킹 - 최소 값을 넘어 버리면 return
                return
        if ans and tmp_sum < min_sum:
            min_sum = tmp_sum
        return
    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            path[cnt] = i
            dfs(cnt+1)
            visited[i] = 0


N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
min_sum = sum(map(sum, [i for i in cost]))  # cost 값들 다 합친 값을 min으로 줌


visited = [0] * (N + 1)
path = [0] * N
dfs(0) # cnt=0을 전달함으로써, 1번~N번까지 순회하는 경우의 수를 만들어주면서 동시에 최소 비용 구함
print(min_sum)

