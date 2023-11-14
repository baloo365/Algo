import sys
T = int(input())
lists = []

for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    lists.append((x, y))

lists.sort(key=lambda x: (x[1], x[0]))

for i in lists:
    print(i[0], i[1])
