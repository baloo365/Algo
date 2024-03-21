# 딕셔너리로 1차 메모리 줄임
# for문을 사용하면 N이 너무 커서 메모리 초과가 남
# 메모이제이션을 통해 이미 있는 값이면 저장되어 있는 값 바로 반환
# 없을 경우 계산을 하고 값을 저장하고 나서 반환한다.

N, P, Q = map(int, input().split())

arr = {}
arr[0] = 1

def dp(n):
    if n not in arr:
        arr[n] = dp(n//P) + dp(n//Q)
    return arr[n]

print(dp(N))
