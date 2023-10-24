import sys

# 재귀함수 w(a, b, c)
# a, b, c 중 0 이하인 수가 하나라도 있으면 1 리턴
# a, b, c 중 20을 넘는 수가 하나라도 있으면 w(20, 20, 20)
# a < b < c일 경우, w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
# 나머지의 경우, w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

def w(a, b, c):
    global dp
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    elif dp[a][b][c]:
        return dp[a][b][c]

    elif a < b and b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]

    else:
        dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return dp[a][b][c]


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    dp = [[[0] * 50 for _ in range(50)] for _ in range(50)]
    # print(dp)
    print(f'w({a}, {b}, {c}) =', w(a, b, c))
