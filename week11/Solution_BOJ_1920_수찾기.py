import sys

F = int(input())
F_list = list(map(int, sys.stdin.readline().split()))
F_list.sort()

S = int(input())
S_list = list(map(int, sys.stdin.readline().split()))

for i in S_list:
    first = 0
    last = F - 1
    result = 0
    while first <= last:
        mid = (first + last) // 2
        if i == F_list[mid]:
            result = 1
            break
        elif F_list[mid] < i:
            first = mid + 1
            result = 0
        else:
            last = mid - 1
            result = 0
    print(result)
