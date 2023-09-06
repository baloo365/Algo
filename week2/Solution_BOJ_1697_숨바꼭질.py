# 수빈이 위치 N, 동생 위치 K
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하라
# -> bfs로 최단 거리 구하는 개념 이용
# 수빈이가 이동할 수 있는 경우의 수
# X+1, X-1, 2*X
# dfs, bfs 관련 문제라는 것을 알고 접근하니까 금방 유추가 되었음.

from collections import deque
def bfs(start_v):
    q.append(start_v)

    while q:
        now = q.popleft()
        if now == K:
            return visited[now]
        for dt in (1, -1, now):
            nt = now + dt
            if 0 <= nt <= 100000 and visited[nt] == 0 :
                visited[nt] = visited[now] + 1    # count 역할
                q.append(nt)

N, K = map(int, input().split())
visited = [0] * 100001     # 범위가 100000 이하이므로 그에 맞게 리스트 생성
q = deque()
print(bfs(N))
