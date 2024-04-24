N = int(input())
arr = sorted(list(map(int, input().split())))
# print(arr)

# 어떤 수가 다른 수 두개의 합으로 나타낼 수 있다면 좋다라고 한다.
# 좋은 수의 개수는 몇 개인지 출력

cnt = 0

for num in range(N):
    start = 0
    end = N - 1
    while start < end:
        if arr[start] + arr[end] == arr[num]:
            if start == num:
                start += 1
            elif end == num:
                end -= 1
            else:
                cnt += 1
                break
        elif arr[start] + arr[end] < arr[num]:
            start += 1
        elif arr[start] + arr[end] > arr[num]:
            end -= 1

print(cnt)

