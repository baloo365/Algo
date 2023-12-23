import sys

N = int(input())
arr = list(map(int,input().split()))
index = list(range(1, N+1))
ans = []

s = 0
temp = arr.pop(s)
ans.append(index.pop(s))

while arr:
    if temp < 0:
        s = (s+temp)%len(arr)
    else:
        s = (s+temp-1)%len(arr)
    temp = arr.pop(s)
    ans.append(index.pop(s))

for i in ans:
    print(i, end=' ')
