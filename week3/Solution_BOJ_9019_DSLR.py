import sys
from collections import deque

T = int(input())

for tc in range(T):
    A, B = map(int, input().split())
    q = deque([(A, '')])
    visited = [0] * 10001
    visited[A] = 1
    while q:

        num, ans = q.popleft()
        if num == B:
            print(ans)
            break

        d = num * 2 % 10000
        if not visited[d]:
            visited[d] = 1
            q.append([d, ans + 'D'])

        s = (num - 1) % 10000
        if not visited[s]:
            visited[s] = 1
            q.append([s, ans + 'S'])

        l = num // 1000 + (num % 1000) * 10
        if not visited[l]:
            visited[l] = 1
            q.append([l, ans + 'L'])

        r = num // 10 + (num % 10) * 1000
        if not visited[r]:
            visited[r] = 1
            q.append([r, ans + 'R'])




