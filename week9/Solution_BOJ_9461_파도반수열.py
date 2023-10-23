import sys

# P(N)을 구하는 프로그램을 작성하시오.
# N은 1이상 100이하
dp = [0] * (101)
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, 101):
    dp[i] = dp[i-2] + dp[i-3]

T = int(input())
for i in range(T):
    N = int(input())
    print(dp[N])
