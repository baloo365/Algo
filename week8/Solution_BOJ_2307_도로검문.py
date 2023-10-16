import sys
import heapq

# 검문을 하는 경우에 대한 지연 시간 구하는 다익스트라
def dijkstra(a, b):
    q = []
    heapq.heappush(q, (0, 1))
    t_lst[1] = 0
    while q:
        time, loca = heapq.heappop(q)

        if loca == N:
            return
        for new_loca, new_time in adj_l[loca]:
          # 검문하는 도로 양끝점일 경우 continue
            if (new_loca == a and loca == b) or (new_loca == b and loca == a):
                continue
            result = time + new_time
            if t_lst[new_loca] > result:
                t_lst[new_loca] = result
                heapq.heappush(q, (result, new_loca))
    return t_lst[N]

# 도로 검문 안 하는 경우의 탈출 시간
def dijkstra2():
    global r_lst
    q = []
    heapq.heappush(q, (0, 1))
    r_lst[1] = 0
    while q:
        time, loca = heapq.heappop(q)
        if loca == N:
            return
        for new_loca, new_time in adj_l[loca]:
            result = time + new_time
            if r_lst[new_loca] > result:
                r_lst[new_loca] = result
                heapq.heappush(q, (result, new_loca))
    return r_lst[N]

N, M = map(int, input().split())
adj_l = [[] for _ in range(N+1)]
road = []
for _ in range(M):
    a, b, t = map(int, input().split())
    adj_l[a].append((b, t))
    adj_l[b].append((a, t))
    road.append((a, b))

# print(road)
# print(adj_l)
INF = 1e9
r_lst = [INF] * (N + 1)
dijkstra2()
ans1 = r_lst[N]
max_result = 0
for lst in road:
    t_lst = [INF] * (N + 1)
    # print(lst)
    dijkstra(*lst)
    # print(t_lst)
    if t_lst[N] == 1e9:
        max_result = -1
        break
    else:
        ans2 = t_lst[N]-r_lst[N]
        # print(ans2)
        max_result = max(max_result, ans2)

print(max_result)
