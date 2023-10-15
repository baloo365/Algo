import sys
import heapq

def dijkstra():
    global c
    INF = 1e9
    result_time = [INF] * (n+1)
    q = []
    heapq.heappush(q, ((0, c)))
    result_time[c] = 0

    while q:
        t, com = heapq.heappop(q)
        for i_com, i_time in adj_l[com]:
            time = i_time + t
            if time < result_time[i_com]:
                result_time[i_com] = time
                heapq.heappush(q, ((time, i_com)))

    return result_time

T = int(input())
# 컴퓨터 개수, 의존성 개수, 해킹당한 컴퓨터 번호
for tc in range(1, T+1):
    n, d, c = map(int, input().split())
    adj_l = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        # a가 b를 의존하며, b가 감염되면 s초 후 a도 감염됨
        # 총 감염되는 컴퓨터 수, 마지막 컴퓨터가 감염되기까지 걸리는 시간
        adj_l[b].append((a, s))

    # print(adj_l)
    temp_ans = dijkstra()
    cnt = 0
    max_result = 0
    for i in temp_ans:
        if i != 1e9:
            cnt += 1
            max_result = max(max_result, i)
    print(cnt, max_result)
