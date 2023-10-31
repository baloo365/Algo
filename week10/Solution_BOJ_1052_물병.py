import sys

N, K = map(int, sys.stdin.readline().split())

result2 = 0
# result_num = num_sum(N)

while bin(N).count('1') > K:
    result_add = 2 ** (bin(N)[::-1].index('1'))
    result2 += result_add
    N += result_add
print(result2)
