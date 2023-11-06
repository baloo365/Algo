import sys
import math

M, N = map(int, sys.stdin.readline().split())

for nums in range(M, N+1):
    result = True
    for num in range(2, round(math.sqrt(nums))+1):
        if nums % num ==0:
            result = False
            break
    if nums == 1:
        result = False
    if result == True:
        print(nums)
