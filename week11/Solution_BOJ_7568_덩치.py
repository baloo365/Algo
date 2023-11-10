import sys

lists = []
all_list = []
T = int(input())

for i in range(T):
    lists = list(map(int, sys.stdin.readline().split()))
    all_list.append(lists)

for i in range(len(all_list)):
    cnt = len(all_list)+1
    for a in range(len(all_list)):
        if (all_list[i][0] >= all_list[a][0]) or (all_list[i][1] >= all_list[a][1]):
            cnt -= 1
    print(cnt, '', end='')
