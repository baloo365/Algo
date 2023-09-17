# dfs 오랜만이라 그런지 헷갈림.
# 답은 잘 구했으나 답 구하기까지 시간이 좀 걸림
# 처음 for문은 1~5번의 사람들 번호(num)이고 그 안의 두번째 for문은 각각의 num과 num을 제외한 나머지 4인과의 관계 단계를 구해서 함  

import sys

N, M = map(int, input().split())
adj_l = [[] for _ in range(N+1)]


def step():
    global friend
    while stack:
        start_v = stack.pop(0)

        if friend in adj_l[start_v]:
            # print('v', visited[start_v])
            return visited[start_v]

        for t in adj_l[start_v]:
            if visited[t] == 0:
                visited[t] = visited[start_v] + 1
                # print('!', t, start_v, visited[t])
                stack.append(t)

    return visited[start_v]


for _ in range(M):
    a, b = map(int, input().split())
    adj_l[a].append(b)
    adj_l[b].append(a)

# print(adj_l)

min_step = N*M
idx = 0
for num in range(1, N+1):
    cnt = 0
    for friend in range(1, N+1):
        if num != friend:
            visited = [0] * (N + 1)
            visited[num] = 1
            stack = [num]
            cnt += step()
            # print('num', num, 'friend', friend)

    if min_step > cnt:
        min_step = cnt
        idx = num

print(idx)
