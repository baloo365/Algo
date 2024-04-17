N = int(input())
arr = list(map(int, input().split()))

arr.sort()

left_pointer = 0
right_pointer = N-1
close_zero = abs(arr[0] + arr[-1])
result = [arr[left_pointer], arr[right_pointer]]
# 첫째 줄에 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액의 특성값 출력

while left_pointer < right_pointer:
    left_value = arr[left_pointer]
    right_value = arr[right_pointer]

    temp_sum = left_value + right_value

    if abs(temp_sum) < close_zero:
        # 0이랑 가까운 경우임
        close_zero = abs(temp_sum)
        result = [left_value, right_value]

    # 음수일 경우, left pointer를 움직여줌
    if temp_sum < 0:
        left_pointer += 1
    else:
        right_pointer -= 1

print(result[0], result[1])



