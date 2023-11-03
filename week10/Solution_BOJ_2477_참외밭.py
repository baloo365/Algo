km = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]
# 동:1, 서:2, 남:3, 북:4

# print(arr)
max_col = 0
max_col_idx = 0
for i in range(6):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if max_col < arr[i][1]:
            max_col = arr[i][1]
            max_col_idx = i


max_row = 0
max_row_idx = 0
for i in range(6):
    if arr[i][0] == 3 or arr[i][0] == 4:
        if max_row < arr[i][1]:
            max_row = arr[i][1]
            max_row_idx = i

big_w = max_row * max_col
# print(big_w)

# 작은 사각형 세로
small_c = abs(arr[(max_col_idx-1) % 6][1] - arr[(max_col_idx+1) % 6][1])
small_r = abs(arr[(max_row_idx-1) % 6][1] - arr[(max_row_idx+1) % 6][1])
# 작은 사각형 가로

ans = big_w - (small_r * small_c)
print(ans*km)
