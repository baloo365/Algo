T = int(input())
 
for tc in range(1, T+1):
    arr = [input() for _ in range(5)]
 
    max_len = 0
    for i in arr:
        if len(i) > max_len:
            max_len = len(i)
 
    for i in range(len(arr)):
        if len(arr[i]) != max_len:
            for _ in range(max_len - len(arr[i])):
                arr[i] += '-'
 
    arr_lst = list(zip(*arr))
 
    result = ''
    for i in arr_lst:
        result += ''.join(i)
 
    result = result.replace('-', '')
    print(f'#{tc} {result}')
