import sys
# def schedule(idx):
#     global temp_price_sum
#     global temp_time
#     global result_price_sum
#     # print(idx, work[idx][1])
#     # print(idx+work[idx][0])
#     if (idx + work[idx][0]) >= N + 1:
#         result_price_sum = max(result_price_sum, temp_price_sum)
#         memo[a] = max(memo[a], temp_price_sum)
#         return
#     for i in range(idx+work[idx][0], N+1):
#         if (i + work[i][0]) > N + 1:
#             result_price_sum = max(result_price_sum, temp_price_sum)
#             memo[a] = max(memo[a], temp_price_sum)
#             return
#         if memo[i] != 0:
#             # print('memo', memo[i])
#             result_price_sum = max(result_price_sum, temp_price_sum+memo[i])
#             memo[a] = max(memo[a], temp_price_sum+memo[i])
#             continue
#         if visited[i] == 0:
#             # print('hi1', i)
#             visited[i] = 1
#             temp_price_sum += work[i][1]
#             schedule(i)
#             visited[i] = 0
#             temp_price_sum -= work[i][1]
#
#
# N = int(input())
# memo = [0] * (N+1)
# work = [[] for _ in range(N+1)]
# for i in range(1, N+1):
#     t, p = map(int, sys.stdin.readline().split())
#     work[i] = (t, p)
#
# result_price_sum = 0
# for a in range(N, 0, -1):
#     if (a+work[a][0]) > N+1:
#         continue
#     temp_time = 0
#     temp_price_sum = work[a][1]
#     visited = [0] * (N+1)
#     visited[a] = 1
#     # print(f'tc{a}')
#     schedule(a)
#
# #   그 전까지는 상관없이 상담을 한 날짜 이후로의 최대값은 같을 것이다.
# #   거꾸로 접근
# print(result_price_sum)
# # print(memo)

# 입력
N = int(input())
work = [[] for _ in range(N+1)]
for i in range(1, N+1):
    t, p = map(int, sys.stdin.readline().split())
    work[i] = (t, p)

# DP
day = [0] * (N + 2)  # 해당 날짜에 최대로 받을 수 있는 돈
for i in range(N, 0, -1):  # 마지막 날부터 첫 날까지 거슬러서 계산
    # N일을 벗어나는 스케줄은 무시
    if i + work[i][0] > N + 1:
        print(i)
        day[i] = day[i + 1]

    # 해당 스케줄을 함으로써 더 돈을 많이 벌면 갱신
    else:
        day[i] = max(day[i + 1], day[i + work[i][0]] + work[i][1])
print(day[1])
