def f(i, N):
    global result
    if i == N:
        new_lst = [1] + p + [1]
        ans = min_p(new_lst)
        # print(ans)
        if ans < result:
            result = ans
        return
    else:
        for j in range(N):
            if used[j] == 0:
                p[i] = arr[j]
                used[j] = 1
                f(i+1, N)
                used[j] = 0
 
 
def min_p(new_lst):
    s = 0
    for i in range(len(new_lst)-1):
        s += cart_a[new_lst[i]-1][new_lst[i+1]-1]
    return s
 
 
T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    cart_a = [list(map(int, input().split())) for _ in range(N)]
    arr = [i for i in range(2, N+1)]
    N = len(arr)
    p = [0] * N
    used = [0] * N
    result = 10000
 
    f(0, N)
    print(f'#{tc} {result}')
