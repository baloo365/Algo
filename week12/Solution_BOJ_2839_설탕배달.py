import sys

N = int(sys.stdin.readline().strip())

T = N // 5
result = 0

if N % 5 != 0: # 5로 나눠떨어지지 않을 때
    while T != -1:
        if (N - (5*T)) % 3 != 0: # 5로 나누고 나서 나머지를 3으로 나눴는데 나눠떨어지지 않을 때
            result = -1
            T -= 1
        else:
            result = T + ((N - (5*T)) // 3)
            break
else:
    result = T

print(result)
