def array(i, j, temp_str):
 
    if len(temp_str) == 7:
        result.add(temp_str)
        return
 
    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ni, nj = i + di, j + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            array(ni, nj, temp_str + arr[ni][nj])
 
 
T = int(input())
 
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    # print(arr)
 
    result = set()
    for i in range(4):
        for j in range(4):
            temp_str = arr[i][j]
            array(i, j, temp_str)
 
    print(f'#{tc} {len(result)}')
