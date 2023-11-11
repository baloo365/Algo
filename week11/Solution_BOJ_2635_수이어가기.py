N = int(input()) # 1 <= N <= 30000
cnt = 0
result_max = 0

def max_count(N, num):
    global cnt
    if N - num < 0:
        return cnt
    cnt += 1
    result_N = N - num
    return max_count(num, result_N)

def result_print(N, num):
    print(N, end=' ')
    print(num, end=' ')
    while N - num >= 0:
        print(N-num, end=' ')
        N, num = num, N-num

for i in range(1, N+1):
    cnt = 0
    func_count = max_count(N, i)
    if result_max < func_count:
        result_max = func_count
        result_num = i

print(max_count(N, result_num))
result_print(N, result_num)
