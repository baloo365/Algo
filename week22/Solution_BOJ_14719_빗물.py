H, W = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(1, W-1):
    left = max(arr[ :i])
    right = max(arr[i+1: ])
    m = min(left, right)
    if m > arr[i]:
        result += m - arr[i]

print(result)
