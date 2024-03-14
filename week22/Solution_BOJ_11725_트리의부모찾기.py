import sys
sys.setrecursionlimit(10**6)

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [0]*(N+1)
visited[1] = 1
def dfs(i):
    for k in tree[i]:
        if visited[k] == 0:
            visited[k] = i
            dfs(k)

dfs(1)

for i in range(2, N+1):
    print(visited[i])
