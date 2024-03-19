def dfs(start_v):
    global temp_cnt
    global visited

    for k in tree[start_v]:
        if visited[k] == 0:
            temp_cnt += 1
            visited[k] = 1
            # print(k, visited)
            dfs(k)


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    tree = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    visited = [0] * (N+1)
    visited[1] = 1
    temp_cnt = 0
    dfs(1)
    print(temp_cnt)
