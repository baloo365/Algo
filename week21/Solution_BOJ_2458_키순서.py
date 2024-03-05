N, M = map(int, input().split()) # N: 학생 수, M: 두 학생 키를 비교한 횟수
big = [[] for _ in range(N+1)]
small = [[] for _ in range(N+1)]

for i in range(M):
    # a인 학생이 b인 학생보다 키가 작음
    a, b = map(int, input().split())
    big[a].append(b)
    small[b].append(a)

# 자신의 키가 몇 번째인지 알 수 있는 학생들이 모두 몇 명인지 출력
# 모두와 연결되어 있는 경우 찾으면 될 듯
# print(big)
# print(small)

def dfs(start_v, prev_v):
    temp_big = big[start_v]
    temp_small = small[start_v]

    if prev_v not in temp_big:
        for student in temp_big:
            if visited[student] == 0:
                visited[student] = 1
                dfs(student, start_v)

    if prev_v not in temp_small:
        for student in temp_small:
            if visited[student] == 0:
                visited[student] = 1
                dfs(student, start_v)


result = 0
for i in range(1, N+1):
    visited = [1] + [0] * (N)
    visited[i] = 1
    dfs(i, i)
    # print(visited)
    if 0 in visited:
        continue
    else:
        result += 1

print(result)
