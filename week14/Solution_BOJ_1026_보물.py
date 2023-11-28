import sys
N = int(input())

A_lst = list(map(int, input().split()))
B_lst = list(map(int, input().split()))

B_lst = sorted(B_lst)
A_lst = sorted(A_lst, reverse=True)

result = 0
for i in range(N):
    result += A_lst[i]*B_lst[i]

print(result)
