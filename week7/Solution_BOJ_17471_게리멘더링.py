import sys
from collections import deque

N = int(input())

# 1번 구역부터 N번 구역까지 순서대로 주어짐.
arr = list(map(int, input().split()))
# 각 구역과 인접한 구역의 정보가 주어진다.
# 첫 번째 정수는 그 구역과 인접한 구역의 수, 이후 인접한 구역의 번호가 주어진다.

# N개의 구역을 두 개의 선거구로 나눔. 각 구역은 두 선거구 중 하나에 포함되어야 함.
# 선거구는 적어도 하나를 포함해야 함.
# 한 선거구에 포함되어 있는 구역은 모두 연결되어 있어야 함
# 중간에 통하는 인접한 구역은 0개 이상
# 모두 같은 선거구에 포함된 구역이어야 한다.
# 두 선거구에 포함된 인구의 차이를 최소로 할 때, 인구 차이의 최솟값을 구해라
# 두 선거구로 나눌 수 없는 경우에는 -1 출력

# 어떻게 구현할 것인지에 대한 생각!
# 1. 하나 이상씩 포함되게 두 그룹으로 나눈다. --> 이를 어떻게 구현할 것인가?
def subset(idx):
    if idx == N:
        temp = []
        temp2 = []
        # print(a)
        for i in range(N):
            if a[i] == True:
                temp.append(i+1)
            else:
                temp2.append(i+1)

        if len(temp) > 0 and len(temp) < N:
            result.append([temp, temp2])
        return

    a[idx] = True
    subset(idx+1)
    a[idx] = False
    subset(idx+1)

# 2. 그 다음 각각의 그룹들이 이어져있는지 확인한다. --> bfs나 dfs로 확인
def bfs1():
    cnt1 = 1     # 이어져 있는지 확인용
    total1 = 0   # 합계
    while q1:
        v = q1.popleft()
        total1 += arr[v-1]
        for t in adj_l[v]:
            if visited1[t] == 0 and (t in section1):
                visited1[t] = 1
                q1.append(t)
                cnt1 += 1

    return total1, cnt1


def bfs2():
    cnt2 = 1  # 이어져 있는지 확인용
    total2 = 0  # 합계
    while q2:
        v = q2.popleft()
        # print(v)
        total2 += arr[v-1]
        for t in adj_l[v]:
            if visited2[t] == 0 and (t in section2):
                visited2[t] = 1
                q2.append(t)
                cnt2 += 1

    return total2, cnt2



adj_l = [[] for _ in range(N+1)]

for i in range(1, N+1):
    n, *lst = map(int, input().split())
    if n != 0:
        adj_l[i] = lst

# print(adj_l)
a = [[] for _ in range(N)]
result = []
subset(0)
ans_result = 100**N+N
# print(result)

for section1, section2 in result:
    visited1 = [0] * (N+1)
    q1 = deque()
    q1.append(section1[0])
    visited1[section1[0]] = 1

    visited2 = [0] * (N+1)
    q2 = deque()
    q2.append(section2[0])
    visited2[section2[0]] = 1

    total1, cnt1 = bfs1()
    total2, cnt2 = bfs2()

    if cnt1 + cnt2 == N:
        # print(cnt1, cnt2, total1, total2)
        temp_sbt = abs(total1-total2)
        if temp_sbt < ans_result:
            ans_result = temp_sbt

    # print(ans_result)

if ans_result == 100**N+N:
    ans_result = -1

print(ans_result)
