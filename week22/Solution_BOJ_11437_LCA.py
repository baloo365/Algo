# LCA란? LCA 알고리즘으로 트리에서 두 노드에 대한 최소 공통 조상을 찾는 알고리즘
# 공통 조상을 구하기 위해서 트리의 깊이(depth)를 이용
# 1단계
# 루트 노드에서 dfs 또는 bfs로 순회하여 전체 노드에 대한 각각의 부모노드와 깊이를 구한다.
# 2단계
# 최소 공통 조상을 구해야 하는 두 노드를 입력 받는다.
# 3단계
# 만약 두 노드의 깊이가 다르다면, 깊이가 더 깊은 노드를 해당 노드의 부모 노드로 바꿔준다.(두 노드의 깊이가 같아질 때까지 반복)
# 깊이가 같다면, 두 노드의 값을 비교한다. 두 노드의 값이 다르다면, 두 노드 모두 해당 노드들의 부모 노드로 바꿔준다.(두 노드의 값이 같아질 때까지 반복)

from collections import deque

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    v1, v2 = map(int, input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)
M = int(input())

visited = [-1] * (N + 1)
visited[1] = 0
parent = [0] * (N + 1)
def make_depth(start_v):
    q = deque()
    q.append(start_v)

    while q:
        v = q.popleft()
        for a in tree[v]:
            if visited[a] == -1:
                visited[a] = visited[v] + 1
                parent[a] = v
                q.append(a)

    return visited

depth_result = make_depth(1)
# print(depth_result)
# print(parent)

def lca(a, b):
    while depth_result[a] != depth_result[b]:
        if depth_result[a] > depth_result[b]:
            a = parent[a]
        else:
            b = parent[b]

    while a != b:
            a = parent[a]
            b = parent[b]

    return a


for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))
