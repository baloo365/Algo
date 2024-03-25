N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)

# 두번째 풀이
for i in range(1, N):
    arr[i][0] += min(arr[i - 1][1], arr[i - 1][2])
    arr[i][1] += min(arr[i - 1][0], arr[i - 1][2])
    arr[i][2] += min(arr[i - 1][0], arr[i - 1][1])

print(min(arr[N-1]))

# dfs로 풀어보려고 했으나 시간 초과로 실패. dp 사용해서 풀었는데,, 쉬운 dp 문제임에도 나는 어려웠음.
# 첫번째 풀이
# visited = [[0] * 3 for _ in range(N)]
# cost = 1e8
# temp_cost = 0
# def dfs(idx, N):
#     global temp_cost
#     global cost
#
#     if temp_cost >= cost:
#         return
#
#     if idx == N:
#         cost = min(cost, temp_cost)
#         return
#
#     # print(temp_cost)
#     # 방문하지 않은 rgb 확인
#     for i in range(3):
#         if visited[idx-1][i] and idx != 0:
#             continue
#
#         if visited[idx][i] == 0:
#             visited[idx][i] = 1
#             temp_cost += arr[idx][i]
#             # 그 다음 집 확인
#             dfs(idx+1, N)
#             visited[idx][i] = 0
#             temp_cost -= arr[idx][i]
#
# dfs(0, N)
# print(cost)
