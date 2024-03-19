# 트리는 사이클이 없는 연결 그래프이며, 트리 내에서 모든 노드(국가)들은 정확히 하나의 경로로만 서로 연결됨
# 따라서, 트리 내의 노드 수가 N개일 때, 간선의 수는 N-1개(비행경로)임
# 모든 노드를 방문하기 위해 필요한 최소 간선의 수와 동일
# DFS 알고리즘을 사용하면 시작 노드(여기서는 국가 1)부터 시작하여 재귀적으로 모든 노드를 방문할 수 있음
# DFS는 탐색 과정에서 각 노드를 정확히 한 번씩 방문함(사이클이 없는 경우) 
# 이 문제에서는 그 과정에서 경로(간선)의 수를 세어, 모든 국가를 방문하기 위해 필요한 최소한의 비행 횟수를 계산함
# 문제를 좀 어렵게 이해해서 dfs로 풀어냄

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
