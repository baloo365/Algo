import heapq

N = int(input())
q = []
max_day = 0

for _ in range(N):
    d, w = map(int, input().split())
    # d는 과제 마감일까지 남은 일수
    # w는 과제 점수
    # 마감일이 지난 과제는 점수를 받을 수 없다.
    # 가장 점수를 많이 받을 수 있도록 과제를 수행
    heapq.heappush(q, (-w, d))

    # 최대 마감일을 넣어준다.
    if max_day < d:
        max_day = d

# 인덱스 때문에 +1 해준다.
max_list = [False] * (max_day + 1)

score = 0
while q:
    w, d = heapq.heappop(q)
    w = -w

    # 비어있는 날에 최대한 늦게 배정한다.
    # 이미 배정된 과제가 있는 경우에는 전날에 배정한다.
    
    for i in range(d, 0, -1):
        if max_list[i]:
            continue

        max_list[i] = True
        score += w
        break

print(score)
