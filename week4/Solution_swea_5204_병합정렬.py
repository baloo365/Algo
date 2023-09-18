T = int(input())


def divide_conquer(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    L_arr = divide_conquer(arr[0:mid])
    R_arr = divide_conquer(arr[mid:N])
    # print(L_arr, R_arr)

    return merge(L_arr, R_arr)


def merge(L_arr, R_arr):
    global cnt
    result = []
    i = 0
    j = 0

    # print(L_arr, R_arr)
    leng_i = len(L_arr)
    leng_j = len(R_arr)

    if L_arr[-1] > R_arr[-1]:
        cnt += 1

    while leng_i > i or leng_j > j:
        if i < leng_i and j < leng_j:
            if L_arr[i] <= R_arr[j]:
                result.append(L_arr[i])
                i += 1
            else:
                result.append(R_arr[j])
                j += 1
        elif i < len(L_arr):
            result.append(L_arr[i])
            i += 1
        elif j < len(R_arr):
            result.append(R_arr[j])
            j += 1

    return result


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    ans = divide_conquer(arr)

    middd = ans[len(arr) // 2]
    print(f'#{tc} {middd} {cnt}')
