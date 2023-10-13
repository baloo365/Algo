import sys
import heapq


def dijkstra(start_i, start_j):
    q = []
    heapq.heappush(q, (arr[start_i][start_j], start_i, start_j))
    distance[start_i][start_j] = 0

    while q:
        dist, now_i, now_j = heapq.heappop(q)
        if now_i == N-1 and now_j == N-1:
            print(f'Problem {tc}: {distance[now_i][now_j]}')
            break

        # if distance[now_i][now_j] < dist:
        #     continue

        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = now_i+di, now_j+dj
            if 0 <= ni < N and 0 <= nj < N:
                # print(ni, nj)
                now_cost = dist + arr[ni][nj]

                if now_cost < distance[ni][nj]:
                    distance[ni][nj] = now_cost
                    heapq.heappush(q, (now_cost, ni, nj))


tc = 1
while True:
    N = int(input())

    if N == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    INF = 1e8
    distance = [[INF] * N for _ in range(N)]
    dijkstra(0, 0)
    tc += 1

