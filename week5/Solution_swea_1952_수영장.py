import sys

def dfs(month, money):
    global min_price
    if month >= 13:
        min_price = min(min_price, money)
        return
    else:
        # 1일권
        dfs(month+1, money+price[0]*plan[month])
        # 1달권
        dfs(month+1, money+price[1])
        # 3달권
        dfs(month+3, money+price[2])

T = int(input())
for test_case in range(1, T+1):
    price = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))

    # 최소값은 1년권으로 잡아둠
    min_price = price[-1]
    dfs(1, 0)
    print(f'#{test_case} {min_price}')
