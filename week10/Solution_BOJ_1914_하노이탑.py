def hanoi(N, start, mid, end):
    if N == 1:
        print(start, end)
    else:
        hanoi(N-1, start, end, mid)
        print(start, end)   # 맨 마지막 가장 큰 원판 옮기는 과정
        hanoi(N-1, mid, start, end)




N = int(input())

print(2**N-1)
if N <= 20:
    hanoi(N, 1, 2, 3)
