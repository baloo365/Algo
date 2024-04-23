N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
is_have = list(map(int, input().split()))
result = []

def binary(number):
    start = 0
    end = N-1
    temp_result = 0

    while start <= end:
        mid = (start + end) // 2
        if number == cards[mid]:
            temp_result = 1
            break
        elif number < cards[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return temp_result

# 상근이가 가지고 있으면 1, 아니면 0을 출력
for number in is_have:
    result.append(binary(number))
print(*result)
