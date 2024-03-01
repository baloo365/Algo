n = int(input())
arr = [[] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

# print(arr)

for i in range(n-1):
    arr[i + 1][0] += arr[i][0]
    arr[i + 1][len(arr[i])] += arr[i][len(arr[i])-1]
    for j in range(1, len(arr[i])):
        arr[i+1][j] += max(arr[i][j-1], arr[i][j])
        # print(arr[i][j], arr[i+1][j], arr[i+1][j+1])
print(max(arr[-1]))
