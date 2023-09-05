import sys
from collections import deque

# dfs() 사용하여 연결된 것끼리 리스트에 넣어주면 될 듯
# 그리고 len() 사용
# 이렇게 하려고 했으나 시간 초과와 재귀 호출 초과(sys.setrecursionlimit(5000)를 통해 해결 가능하지만)
# 마지막 코드 부분에서 방문하지 않았을 때, 연결된 노드들이 없을 때 등 가지치기를 통해 시간 단축
# dequeue의 popleft()를 통해서 시간 단축

def bfs(i):
    q = deque([i])
    visited[i] = 1
    while q:
        v = q.popleft()
        for j in adj_list[v]:
            if visited[j] == 0:
                visited[j] = 1
                q.append(j)


N, M = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(N+1)]
result = []
visited = [0] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

# print(adj_list)

cnt = 0
for i in range(1, N+1):
    if visited[i] == 0: # 방문하지 않았을 때
        if not adj_list[i]:
            cnt += 1
            visited[i] = 1
        else:
            bfs(i)
            cnt += 1

# print(result)
print(cnt)
