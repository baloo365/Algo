N, M = map(int, input().split()) #
city = [list(map(int, input().split())) for _ in range(N)]
# print(city)

chicken = []
home_list = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home_list.append((i, j))

        if city[i][j] == 2:
            chicken.append((i, j))


# 1. 치킨집 M를 조합으로 추린다.
combi_list = []
def combi(idx, temp_list):
    if len(temp_list) == M:
        combi_list.append(temp_list[:])
        return

    for i in range(idx, len(chicken)):
        combi(i + 1, temp_list + [chicken[i]])

combi(0, [])
# print(combi_list)

# 2. 조합에 따른 도시의 치킨 거리를 구한다.
ans = 0

temp_result = N ** N
for stores in combi_list:
    store_sum = 0
    for home_i, home_j in home_list:
        close_chicken = N*N
        for si, sj in stores:
            close_chicken = min(close_chicken, (abs(si - home_i) + abs(sj - home_j)))
        store_sum += close_chicken
        # print((home_i, home_j), stores, store_sum)
    temp_result = min(temp_result, store_sum)
ans += temp_result
print(ans)
