# set이 시간 초과 문제 해결해줌

import sys
import heapq


N, M = map(int, sys.stdin.readline().strip().split())
q = []
nolisten = set()

for _ in range(N):
   nolisten.add(sys.stdin.readline().strip())

for _ in range(M):
    nosee = sys.stdin.readline().strip()
    if nosee in nolisten:
        heapq.heappush(q, nosee)

print(len(q))
while q:
    print(heapq.heappop(q))
