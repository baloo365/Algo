import sys

T = int(input())
result = []

for i in range(T):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    result.append((age, name))

result.sort(key = lambda x: x[0])

for i in result:
    print(i[0], i[1])
