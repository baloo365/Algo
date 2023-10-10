import sys

# N*N에서 이뤄지는 게임이다.
# 보드 곳곳에는 몇 개의 지뢰가 숨겨있음
# 칸을 하나씩 여는데 그 칸에 지뢰가 있다면 게임이 끝나고
# 없는 경우에는 그 칸에 적혀 있는 숫자 인접한 8개 칸에 있는 지뢰 수 알려줌
# 테두리는 모두 열려있고, 그 외 칸들은 닫혀있는 상태로 시작
# 닫혀 있는 칸들 중 최대 몇 개의 칸에 지뢰가 묻혀있는지 알아내시오
# 1<= N <= 100

def bomb():
    global result
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            # if i == 0 or j == 0 or i == N-1 or j == N-1:
            is_bomb = True  # 지뢰가 있는지 없는지 판단용 변수
            # 테두리가 아닌 '#' 칸에서 인접 8칸 탐색
            if arr[i][j] == '#':
                for di, dj in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
                    ni, nj = i + di, j + dj
                    # 인접 8칸 탐색하는데 테두리만
                    if (ni == 0 or ni == N-1) or (nj == 0 or nj == N-1):
                        # 지뢰가 없을 경우, arr[i][j] = ''
                        if arr[ni][nj] == '0':
                            arr[i][j] = ''
                            is_bomb = False

            # print('hi', arr)
            # 인접한 곳에 지뢰가 0인 게 없을 경우
            # print(is_bomb)
            if not is_bomb:
                result -= 1
                
            if is_bomb:
                arr[i][j] = '*'
                for di, dj in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and (arr[ni][nj] != '#' and arr[ni][nj] != '' and arr[ni][nj] != '*'):
                        arr[ni][nj] = str(int(arr[ni][nj]) - 1)
                        
    if N == 1:
       result = 0
    return


N = int(input())
arr = [list(input()) for _ in range(N)]
# print(arr)
result = (N-2)**2
# bomb_loca = []
# for i in range(1, N-2):
#     for j in range(1, N-2):
#         bomb_loca.append((i, j))

bomb()
print(result)
