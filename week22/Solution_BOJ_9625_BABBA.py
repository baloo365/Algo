K = int(input())
# A ->
# B -> BA -> BAB -> BABBA -> BABBA BAB -> BABBABABBABBA
# 0, 1 -> 1, 1 -> 1, 2 -> 2, 3 -> 3, 5 -> 5, 8 ->
# A는 이전 B의 개수, B는 A와 B의 개수


temp = [(0, 1), (1, 1), (1, 2), (2, 3)]
# print(len(temp))

for i in range(4, 46):
    # print(temp[i-1][1], temp[i-1][0] + temp[i-1][1])
    temp.append((temp[i-1][1], temp[i-1][0] + temp[i-1][1]))

# for i in range(K):
#     temp[i]
#
# cnt = 0
# temp[0] = (0, 1)
print(*temp[K-1])
