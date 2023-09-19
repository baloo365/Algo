import sys

T = int(input())

def work(ans, idx):
    global result
    if ans < result:
        return

    if idx == N:
        result = ans

    else:
        for i in range(N):
            if visited[i] == 0 and p_lst[idx][N_lst[i]] != 0:
                r_lst[idx] = N_lst[i]
                visited[i] = 1
                ans *= (p_lst[idx][N_lst[i]])/100
                work(ans, idx+1)
                ans /= (p_lst[idx][N_lst[i]])/100
                visited[i] = 0


for tc in range(1, T+1):
    # 직원 수 N명, 해야할 일 N개
    N = int(input())
    N_lst = [i for i in range(N)]
    r_lst = [0] * N
    p_lst = [[] for _ in range(N)]
    result = 0
    for i in range(N):
        p_lst[i] = list(map(int, input().split()))

    # print(p_lst, N_lst)
    visited = [0] * N
    work(100, 0)
    print(f'#{tc} {result:.6f}')
