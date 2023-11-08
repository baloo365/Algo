p_row, p_col = map(int, input().split())
N = int(input())

row_num = [0]
col_num = [0]

for _ in range(N):
    c_type, num = map(int, input().split()) # row는 0
    if c_type == 0:
        row_num += [num]
    else:
        col_num += [num]

row_num = sorted(row_num) + [p_col]
col_num = sorted(col_num) + [p_row]

row_max = 0
col_max = 0

# print(row_num)
# print(col_num)

for i in range(len(row_num)-1):
    t_sum = row_num[i+1] - row_num[i]
    # print(row_num[i], row_num[i+1])
    if row_max < t_sum:
        row_max = t_sum

for i in range(len(col_num)-1):
    t_sum = col_num[i + 1] - col_num[i]
    # print(col_num[i], col_num[i + 1])
    if col_max < t_sum:
        col_max = t_sum

print(row_max*col_max)
