import heapq
 
 
def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0
 
    while pq:
        dist, now = heapq.heappop(pq)
 
        if distance[now] < dist:
            continue
 
        for next in adj_l[now]:
            next_node = next[0]
            cost = next[1]
            new_cost = dist + cost
 
            if distance[next_node] <= new_cost:
                continue
 
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))
 
T = int(input())
 
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adj_l = [[] for _ in range(N+1)]
 
    INF = int(1e9) 
    distance = [INF] * (N+1)
 
    for i in range(E):
        # 시작, 끝, 구간 거리
        s, e, w = map(int, input().split())
        adj_l[s].append([e, w])
 
    dijkstra(0)
    print(f'#{tc} {distance[-1]}')
