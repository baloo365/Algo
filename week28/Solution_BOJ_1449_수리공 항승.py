# N 물이 새는 곳 개수, L 테이프의 길이
N, L = map(int, input().split())
# 물이 새는 곳의 위치
# 테이프를 붙였을 때, 적어도 여분이 1 있어야 한다.
arr = sorted(list(map(int, input().split())))
# print(arr)

tape_length_sum = 0
start_location = 0
cnt = 0

while start_location < N:
    cnt += 1
    tape_length_sum = 0
    a = start_location + 1
    while a < N:
        tape_length_sum += (arr[a]-arr[a-1])
        if tape_length_sum >= L:
            tape_length_sum = 0
            break
        a += 1
    start_location = a
print(cnt)
