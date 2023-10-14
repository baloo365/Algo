import sys
import heapq

# N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있음
# N명의 학생이 X번 마을에 모여서 파티를 벌이기로 함.
# 마을 사이에는 M개의 단방향 도로들이 있고 i번째 길을 지나는데의 시간을 소비한다.
# 파티에 참서하기 위해 걸어가서 다시 그들의 마을로 돌아와야 함.
# 최단 시간에 오고 가기를 원함.
# 오고 가는 길이 다름. N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구?


def dijkstra(start):
    q = []
    INF = 1e8
    t = [INF] * (N+1)
    heapq.heappush(q, (0, start))
    t[start] = 0

    while q:
        time, town = heapq.heappop(q)
        for v_town, v_time in road[town]:
            v_time += time
            # print(v_time, v_town)
            if v_time < t[v_town]:
                t[v_town] = v_time
                heapq.heappush(q, (v_time, v_town))
    return t

N, M, X = map(int, input().split())
# start, end, time
road = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, time = map(int, input().split())
    road[a].append((b, time))

result = [0] * (N+1)
ans = 0
for i in range(1, N+1):
    s = dijkstra(i)
    e = dijkstra(X)
    ans = max(ans, s[X] + e[i])

print(ans)

