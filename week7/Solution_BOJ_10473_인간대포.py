import sys
import heapq

# 5m/s 속도로 달린다.
# 대포는 원하는 임의의 방향으로 50m 날려준다.
# 대포에 올라타고 발사되어 착륙되기까지 2초가 걸린다.

# 어떻게 구현할 것인가?
# 출발지에서 목적지까지 걸리는 시간을 구한다.

def run(loca1, loca2):
    distance = ((abs(loca1[0] - loca2[0])**2) + (abs(loca1[1] - loca2[1])**2))**0.5
    run_time = distance / 5
    return run_time


def daepo(loca1, loca2):
    distance = ((abs(loca1[0] - loca2[0])**2) + (abs(loca1[1] - loca2[1])**2))**0.5
    daepo_time = (abs(distance - 50) / 5) + 2
    return daepo_time


def dijkstra():
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        tm, idx = heapq.heappop(q)
        if v[idx] != 0:
            continue
        v[idx] = 1
        # 각 지점마다 해당 지점과 출발 지점을 제외한 모든 지점과의 run시간과 daepo 시간을 계산해서
        # 최소값을 구해놓음.
        for i in range(1, N + 3):
            if i == idx:
                continue
            time = run(arr[idx - 1], arr[i - 1])
            # 출발점과 도착점이 아닐 때 걸린 시간은 daepo 시간이랑 run 시간 중 최소값으로 저장
            if idx != 1 and idx != (N + 2):
                time = min(time, daepo(arr[idx - 1], arr[i - 1]))
            if time + tm < t[i]:
                t[i] = time + tm
                heapq.heappush(q, [t[i], i])
    print(t[N + 2])

arr = []
start_x, start_y = map(float, input().split())
end_x, end_y = map(float, input().split())
arr.append((start_x, start_y))
N = int(input())

for _ in range(N):
    x, y = map(float, input().split())
    arr.append((x, y))
arr.append((end_x, end_y))

INF = 1e8
t = [INF] * (N+3)
v = [0] * (N+3)

dijkstra()
