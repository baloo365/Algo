import sys
from collections import deque

T = int(sys.stdin.readline().strip())
dq = deque()

for i in range(1, T + 1):
    dq.append(i)

while len(dq) != 1:
    dq.popleft()
    pop_num = dq.popleft()
    dq.append(pop_num)

print(dq[0])
    
    
