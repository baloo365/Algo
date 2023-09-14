import sys
from collections import deque


def bfs(start_v):
    global ans
    if start_v == max([p1, p2]):
        ans = visited[start_v]-1
        return

    while q:
        t = q.popleft()
        for t_item in adj_lst[t]:
            if not visited[t_item]:
                visited[t_item] = visited[start_v] + 1
                q.append(t_item)
                bfs(t_item)



N = int(input())

p1, p2 = map(int, input().split())
start_v = min(p1, p2)

m = int(input())
adj_lst = [[] for _ in range(N+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

q = deque()
ans = -1
visited = [0] * (N+1)
q.append(start_v)
visited[start_v] = 1
bfs(start_v)
print(ans)
