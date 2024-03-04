T = int(input())
# 행성계 간의 이동을 최대한 피해서 여행해야 한다.
# 원은 행성계의 경계를 의미
# 최소의 행성계 진입/이탈 횟수를 구해라

# 출발점이나 도착점이 어떤 행성 안에 있다면 이 행성을 진입/벗어날 때 이탈/집입한 횟수
# -> 출발점과 어떤 행성의 중심 거리가 그 행성의 반지름보다 작은 경우
# 출발점과 도착점이 어떤 행성 안에 있다면 이 행성을 진입/벗어날 때 이탈/집입한 횟수
# -> 출발점과 도착점 모두 어떤 행성과의 중심 거리가 그 행성의 반지름보다 작은 경우

for tc in range(1, T+1):
    x1, y1, x2, y2 = map(int, input().split()) # 출발점과 도착점
    n = int(input())
    planet = [[] for _ in range(n+1)]

    cnt = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split()) # 중점과 반지름
        start_v = (cx - x1) ** 2 + (cy - y1) ** 2
        end_v = (cx - x2) ** 2 + (cy - y2) ** 2

        if start_v < r**2 and end_v < r**2:
            pass

        elif start_v < r**2:
            cnt += 1
        elif end_v < r**2:
            cnt +=1

    # print(start_list)
    # print(end_list)

    print(cnt)
