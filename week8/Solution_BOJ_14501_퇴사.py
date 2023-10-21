import sys

def schedule(idx):
    global temp_price_sum
    global temp_time
    global result_price_sum
    # print(idx, work[idx][1])
    # print(idx+work[idx][0])
    if (idx + work[idx][0]) >= N + 1:
        result_price_sum = max(result_price_sum, temp_price_sum)
        memo[a] = max(memo[a], temp_price_sum)
        return
    for i in range(idx+work[idx][0], N+1):
        if (i + work[i][0]) > N + 1:
            result_price_sum = max(result_price_sum, temp_price_sum)
            memo[a] = max(memo[a], temp_price_sum)
            continue
        if memo[i] != 0:
            # print('memo', memo[i])
            result_price_sum = max(result_price_sum, temp_price_sum+memo[i])
            memo[a] = max(memo[a], temp_price_sum+memo[i])
            continue
        if visited[i] == 0:
            # print('hi1', i)
            visited[i] = 1
            temp_price_sum += work[i][1]
            schedule(i)
            visited[i] = 0
            temp_price_sum -= work[i][1]


N = int(input())
memo = [0] * (N+1)
work = [[] for _ in range(N+1)]
for i in range(1, N+1):
    t, p = map(int, sys.stdin.readline().rstrip().split())
    work[i] = (t, p)

result_price_sum = 0
for a in range(N, 0, -1):
    if (a+work[a][0]) > N+1:
        continue
    temp_time = 0
    temp_price_sum = work[a][1]
    visited = [0] * (N+1)
    visited[a] = 1
    # print(f'tc{a}')
    schedule(a)

#   그 전까지는 상관없이 상담을 한 날짜 이후로의 최대값은 같을 것이다.
#   거꾸로 접근
print(result_price_sum)
# print(memo)
