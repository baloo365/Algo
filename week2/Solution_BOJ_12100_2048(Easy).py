import sys
from copy import deepcopy



# 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록 출력한다.
# 5번을 상, 하, 좌, 우 어떻게 할 것인가
# 상, 하, 좌, 우 -> 0, 1, 2, 3

# 게임 경우의 수: 1. 0일 때, 2. 같을 때, 3. 다를 때
def move(location):
    board = deepcopy(origin_board)
    for direction in location:
        if direction == 0: # 상
            for j in range(N):
                top = 0
                for i in range(1, N):
                    if board[i][j]:
                        tmp = board[i][j]
                        board[i][j] = 0
                        if board[top][j] == 0:
                            board[top][j] = tmp
                        elif board[top][j] == tmp:
                            board[top][j] = tmp * 2
                            top += 1
                        else:
                            top += 1
                            board[top][j] = tmp

        elif direction == 1:   # 하
            for j in range(N):
                top = N - 1
                for i in range(N - 2, -1, -1):
                    if board[i][j]:
                        tmp = board[i][j]
                        board[i][j] = 0
                        if board[top][j] == 0:
                            board[top][j] = tmp
                        elif board[top][j] == tmp:
                            board[top][j] = tmp * 2
                            top -= 1
                        else:
                            top -= 1
                            board[top][j] = tmp

        elif direction == 2:   # 좌
            for i in range(N):
                top = 0
                for j in range(1, N):
                    if board[i][j]:
                        tmp = board[i][j]
                        board[i][j] = 0
                        if board[i][top] == 0:
                            board[i][top] = tmp
                        elif board[i][top] == tmp:
                            board[i][top] = tmp * 2
                            top += 1
                        else:
                            top += 1
                            board[i][top] = tmp

        elif direction == 3:   # 우
            for i in range(N):
                top = N - 1
                for j in range(N - 2, -1, -1):
                    if board[i][j]:
                        tmp = board[i][j]
                        board[i][j] = 0
                        if board[i][top] == 0:
                            board[i][top] = tmp
                        elif board[i][top] == tmp:
                            board[i][top] = tmp * 2
                            top -= 1
                        else:
                            top -= 1
                            board[i][top] = tmp
    return board



def dfs(a):
    global result
    if a == 5:
        ans = max(map(max, move(location)))
        if ans > result:
            result = ans
        return
    for i in range(4):
        location[a] = i
        dfs(a+1)

N = int(input())
origin_board = [list(map(int, input().split())) for _ in range(N)]
location = [None] * 5
result = 0
dfs(0)
print(result)
