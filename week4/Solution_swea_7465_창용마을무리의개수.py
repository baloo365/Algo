import sys
from collections import deque

def bfs():
    while q:
        t_lst = adj_l[q.popleft()]
        for t in t_lst:
            if visited[t] == 0:
                # print(t)
                visited[t] = 1
                q.append(t)




T = int(input())

for tc in range(1, T+1):
    # 사람 수, 관계 수
    N, M = map(int, input().split())
    adj_l = [[] for _ in range(N+1)]

    for i in range(M):
        a, b = map(int, input().split())
        adj_l[a].append(b)
        adj_l[b].append(a)

    # print(adj_l)
    cnt = 0
    visited = [0] * (N + 1)
    for i in range(1, N+1):
        if visited[i] == 0:
            cnt += 1
            q = deque()
            q.append(i)
            bfs()
    print(f'#{tc} {cnt}')

