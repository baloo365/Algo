T = int(input())
 
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    max_home = 0
    ans = 0
    for i in range(N):
        for j in range(N):
            home_cnt = 0
            k = 1
            cost = 0
            while N+2 >= k:
                if k == 1:
                    if arr[i][j] == 1:
                        home_cnt += 1
                        # print('%', i, j, home_cnt)
 
                elif k == 2:
                    # print('hi')
                    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:   # 우 하 좌 상
                        if 0<= i + di <=N-1 and 0<= j + dj <=N-1 and arr[i + di][j + dj] == 1:
                            home_cnt += 1
                            # print('!', i, j, home_cnt)
 
                else:
                    # print('hello')
                    home_cnt = 0
                    s, e = j, j
                    for p in range(i - (k - 1), i + (k + 1)):
                        for j in range(s, e+1):
                            # print(p, j)
                            if 0 <= p <= N - 1 and 0 <= j <= N - 1 and arr[p][j] == 1:
                                home_cnt += 1
 
                        if p < i:
                            s -= 1
                            e += 1
                        else:
                            s += 1
                            e -= 1
 
                cost = (home_cnt * M) - (k ** 2 + (k - 1) ** 2)
                # print(home_cnt, k, cost)
 
                k += 1
 
                if cost >= 0 and (max_home <= home_cnt):
                    max_home = home_cnt
                    ans = home_cnt
 
 
 
    print(f'#{tc} {ans}')
