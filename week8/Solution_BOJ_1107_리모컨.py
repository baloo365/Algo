import sys

N = int(input())
M = int(input())
if M != 0:
    b_button = list(map(int, input().split()))
else:
    b_button = []
# temp_str = ''
#
# if int(N) == 100:
#     ans = 0
# # print(b_button)
# else:
#     for n in N:
#         min_gap = 10
#         gap_num = 10
#         for i in range(10):
#             if i not in b_button:
#                 # print(i, i-int(n))
#                 gap = abs(i-int(n))
#                 if gap < min_gap:
#                     min_gap = gap
#                     gap_num = i
#                 # print(min_gap)
#         temp_str += str(gap_num)
#     print(temp_str)
#     ans = len(temp_str) + abs(int(temp_str)-int(N))
#
# print(ans)

ans = abs(N-100)

if N == 100:
    ans = 0
else:
    for num in range(1000001):
        num = str(num)
        for i in range(len(num)):
            if (int(num[i]) in b_button):
                break
            elif (i == len(num)-1):
                ans = min(ans, abs(int(num)-N)+len(num))

print(ans)
