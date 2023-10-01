T = int(input())
 
 
def quick_sort(arr, start, end):
    if start >= end:
        return
 
    pivot = start
    i = start + 1
    j = end
 
    # j가 i보다 큰 경우에만 진행
    while i <= j:
 
        # 왼쪽부터 피벗보다 큰 경우
        while i <= end and arr[i] <= arr[pivot]:
            i += 1
 
        # 오른쪽부터 피벗보다 작은 경우
        while j > start and arr[j] >= arr[pivot]:
            j -= 1
 
        if i > j:  # 엇갈릴 경우 피벗이랑 제일 작은 값 바꿔줌
            # print(i, pivot)
            arr[j], arr[pivot] = arr[pivot], arr[j]
 
        else:  # 엇갈리지 않은 경우 i랑 j랑 바꿔줌.
            arr[i], arr[j] = arr[j], arr[i]
 
    quick_sort(arr, start, j - 1)  # 분할 이후 왼쪽
    quick_sort(arr, j + 1, end)  # 분할 이후 오른쪽
 
 
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
 
    start = 0
    end = len(arr)-1
    quick_sort(arr, start, end)
    print(f'#{tc}', arr[N//2])
