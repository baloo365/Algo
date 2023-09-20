# 집합을 만들어주는 과정
# parent = [i for i in range(10)]

# find-set, 부모를 찾아가는 과정
def find_set(x):
    if parent[x] == x:
        return x

    return find_set(parent[x])

# union
def union(x, y):
    # 이미 같은 집한인지 체크
    x = find_set(x)
    y = find_set(y)

    # 대표자가 같으니, 같은 집합이다.
    if x == y:
        return
    # 다른 집합이라면, 같은 대표자로 수정
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = list(range(N+1))

    for i in range(M):
        union(arr[i*2], arr[i*2+1])

    for i in range(N+1):
        parent[i] = find_set(i)

    print(f'#{tc} {len(set(parent))-1}')

    # print(arr)



