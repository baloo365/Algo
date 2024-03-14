# 루트 노드나 리프노드가 아니더라도 어떠한 노드에서 가장 먼 거리가 지름의 양 끝점 중 하나이다.
# 따라서 임의의 노드에서 가장 먼 노드를 구한 후, 그 노드에서 가장 먼 노드까지의 거리가 지름의 길이이다.

import sys
sys.setrecursionlimit(10**6)

V = int(input()) # 트리 정점의 개수
tree = [[] for _ in range(V+1)]
for i in range(1, V+1):
    temp = list(map(int, input().split()))
    for i_line in range(1, len(temp)-1, 2):
        tree[temp[0]].append((temp[i_line], temp[i_line+1]))


def dfs(start_v, dist, visited):
    for n_node, n_dist in tree[start_v]:
        if visited[n_node] == -1:
            visited[n_node] = dist + n_dist
            dfs(n_node, dist + n_dist, visited)
    return


visited = [-1] * (V+1)
visited[1] = 0
dfs(1, 0, visited)

max_node = visited.index(max(visited))

visited = [-1] * (V+1)
visited[max_node] = 0
dfs(max_node, 0, visited)

print(max(visited))
