N, K = map(int, input().split())
arr = list(map(int, input().split()))
result_min = [arr[i] for i in range(K)]
first_sum = sum(result_min)
max_sum = sum(result_min)

for i in range(K, N):
    first_sum = first_sum - arr[i-K] + arr[i]

    if max_sum < first_sum:
        max_sum = first_sum

print(max_sum)
