import sys

T = int(input())
result = []

for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    result.append((x, y))

result.sort(key=lambda x: (x[0], x[1]))

for i in result:
    print(i[0], i[1])
