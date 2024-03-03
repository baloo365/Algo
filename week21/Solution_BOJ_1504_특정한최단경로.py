import heapq
# 방향성이 없는 그래프
# 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동
# 임의의 두 정점은 반드시 통과 해야 한다.
# 두 개의 정점을 지나는 최단 경로의 길이를 출력
# 그러한 경로가 없을 때에는 -1을 출력

N, E = map(int, input().split()) # 정점의 개수 N과 간선의 개수 E
arr = [[] for _ in range(N+1)]

for i in range(E):
    a, b, c = map(int, input().split()) # a정점, b정점, c거리
    arr[a].append((c, b))
    arr[b].append((c, a))

v1, v2 = map(int, input().split())

# v1 -> v2를 거치는 버전
# v2 -> v1를 거치는 버전

INF = 1e8
def dijkstra(start):
    q = []
    distance = [INF] * (N+1)
    distance[start] = 0 # 시작 점 거리 0에서 시작
    heapq.heappush(q, (0, start))

    while q:
        dist, index = heapq.heappop(q)

        if distance[index] < dist:
            continue

        for i in arr[index]:
            if dist + i[0] < distance[i[1]]:
                distance[i[1]] = dist + i[0]
                heapq.heappush(q, (dist + i[0], i[1]))

    return distance


start_0 = dijkstra(1)
start_v1 = dijkstra(v1)
start_v2 = dijkstra(v2)

# v1를 먼저 지나갈 때
result_v1 = start_0[v1] + start_v1[v2] + start_v2[N]
result_v2 = start_0[v2] + start_v2[v1] + start_v1[N]

ans = min(result_v1, result_v2)
if ans >= INF:
    ans = -1
    
print(ans)
