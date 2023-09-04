def dfs(start_c):
    birus[start_c] = 1

    for i in adj_lst[start_c]:
        if birus[i] == 0:
            dfs(i)


N = int(input())
pair = int(input())

adj_lst = [[] for _ in range(N+1)]

for _ in range(pair):
    a, b = map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

# print(adj_lst)
birus = [0] * (N+1)
dfs(1)
print(sum(birus)-1) # 1번 제외해줌
