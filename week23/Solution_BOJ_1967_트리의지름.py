import sys
sys.setrecursionlimit(10**6)

n = int(input()) # 노드의 개수
tree = [[] for _ in range(n+1)]

# 첫번째는 부모 노드, 두번째는 자식 노드, 세번째는 간선의 가중치
# 부모 노드의 작은 것이 먼저 입력
# 부모 노드의 번호가 같으면 자식 노드의 번호가 작은 것이 먼저 입력
# 루트 노드의 번호는 항상 1
# 모든 경로 중 가장 긴 것의 길이를 구하라
# 끝의 노드들에서 2개 선택...?


for i in range(n-1):
    parent, child, weight = map(int, input().split())
    tree[parent].append([child, weight])
    tree[child].append([parent, weight])
# print(tree)

def dfs(start_v, dist):
    for n_node, n_dist in tree[start_v]:
        if visited[n_node] == -1:
            visited[n_node] = dist + n_dist
            dfs(n_node, dist + n_dist)

visited = [-1] * (n+1)
visited[1] = 0
dfs(1, 0)
max_node = visited.index(max(visited))

visited = [-1] * (n+1)
visited[max_node] = 0
dfs(max_node, 0)

print(max(visited))

