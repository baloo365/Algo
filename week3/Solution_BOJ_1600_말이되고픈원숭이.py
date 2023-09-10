import sys
from collections import deque


def move():
    horse = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
    monkey = ((0, 1), (1, 0), (0, -1), (-1, 0))

    visited = [[[-1] * (K + 1) for _ in range(W)] for _ in range(H)] # (K에 +1 해준 이유는 horse_cnt는 1부터 시작하므로 인덱스 맞춰주려고)
# [0]이 아닌 [-1]을 해준 이유 arr = [0]일 경우 고려하고, 시작점 방문 체크를 0으로 할 경우의 재방문 방지
# K개 만큼 리스트 안에 0을 만들어주는 이유는 horse_cnt=0일 때, horse_cnt=1일 때 방문 처리 구분해주려고
# ex. (2,1)은 말 걸음으로 한방에 갈 수 있기도 하고, (1,0)->(2,0)->(2,1)로 말 걸음 없이 원숭이 걸음으로 3번에 갈 수 있는데
# 이는 각각 방문했는지 여부를 visited[2][1][1], visited[2][1][0]을 보기 때문에 다른 경우로 봐서 중복으로(?) 이동 가능함
    visited[0][0][0] = 0

    q = deque([(0, 0, 0, 0)])

    while q:
        i, j, moves, horse_moves = q.popleft()

        if i == H - 1 and j == W - 1:
            return moves

        for di, dj in horse:
				# 말처럼 이동한 횟수가 아직 K보다 작은 경우 말처럼 이동 가능
            if horse_moves < K:
                ni, nj = i + di, j + dj
                if 0 <= ni < H and 0 <= nj < W and visited[ni][nj][horse_moves + 1] == -1 and arr[ni][nj] == 0:
								# horse_moves + 1로 말 걸음으로 갈 때마다 계층을 바꾸는(?) visited를 리셋(?) 해주는 느낌
								# 동일한 horse_moves값에 해당하는 모든 위치는 동일한 층으로 봄. 다르면 다른 층으로 봄.
								# horse_moves(말처럼 이동)에 따라 방문 처리를 다르게 처리
                    visited[ni][nj][horse_moves + 1] = 1
                    q.append((ni, nj, moves + 1, horse_moves + 1))

        for di, dj in monkey:
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W and visited[ni][nj][horse_moves] == -1 and arr[ni][nj] == 0:
                visited[ni][nj][horse_moves] = 1
                q.append((ni, nj, moves + 1, horse_moves))

    return -1


K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]

# 원숭이가 최소한의 동작으로 맨 왼쪽 위에서 맨 오른쪽 아래로 가는 방법 구함
# 출력은 최소 이동 횟수, 갈 수 없는 경우엔 -1 출력
# 0은 아무것도 없는 평지, 1은 장애물
# K번 나이트처럼 움직일 수 있고 그 외에 상하좌우로 이동
print(move())
