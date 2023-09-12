A, P = map(int, input().split())
# print(A, P)

# 각 자리의 수를 구하는 법
D = [A]

tmp = 0
idx = 0
while True:
    A_lst = list(map(int, str(D[-1])))
    # print(A_lst, tmp, D)
    for i in A_lst:
        tmp += i**P
    if tmp in D:
        idx = D.index(tmp)
        break
    else:
        D.append(tmp)
    tmp = 0

print(idx)
