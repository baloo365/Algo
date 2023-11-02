N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()

max_h = 0
max_h_idx = 0

for i in range(N):
    if arr[i][1] >= max_h:
        max_h = arr[i][1]
        max_h_idx = i

h = arr[0][1]
result = max_h

for i in range(max_h_idx):
    if h < arr[i+1][1] : # 다음 기둥이 더 높을 경우
        result += h * (arr[i + 1][0] - arr[i][0])
        h = arr[i+1][1]

    else:
        result += h * (arr[i + 1][0] - arr[i][0])

h = arr[-1][1]

for i in range(N-1, max_h_idx, -1):
    if h < arr[i - 1][1]:  # 다음 기둥이 더 높을 경우
        result += h * (arr[i][0] - arr[i - 1][0])
        h = arr[i - 1][1]

    else:
        result += h * (arr[i][0] - arr[i-1][0])

print(result)
