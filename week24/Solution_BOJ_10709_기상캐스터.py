H, W = map(int, input().split())
cloud = [list(input()) for _ in range(H)]
# print(cloud)
# 구름이 있는 경우에는 영어 소문자 'c'
# 구름이 없는 경우에는 문자 '.'
# 출력은 H 행으로
# 지금부터 몇 분 후에 처음으로 구역(i, j)에 구름이 뜨는지 표시한다.
# 처음부터 구름이 떠있었던 경우에는 0,
# 몇분이 지나도 구름이 뜨지 않을 경우에는 -1 출력
# 1분마다 오른쪽으로 구름이 이동
# 각 구역에 대해서 지금부터 몇 분 뒤 처음으로 하늘에 구름이 오는지 구하라

result = [[-1] * W for _ in range(H)]
cnt = 1

for i in range(H):
    for j in range(W):
        if cloud[i][j] == 'c':
            result[i][j] = 0
# print(result)

def move_cloud():
    for i in range(H):
        for j in range(W-1, 0, -1):
            cloud[i][j] = cloud[i][j-1]
        cloud[i][0] = '.'
    # print(cloud)

while cnt < W:
    # print(cnt)
    move_cloud()
    # print(cloud)
    for i in range(H):
        for j in range(W):
            if cloud[i][j] == 'c' and result[i][j] == -1:
                result[i][j] = cnt
    cnt += 1
# print(result)
for i in result:
    print(*i)
