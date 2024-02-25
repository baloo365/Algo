import sys

sys.stdin = open("input.txt")

# 길이가 N인 벨트가 있고
# 길이가 2N인 벨트가 감싸며 돌고 있다
# 2N 다음이 1
# 1번 칸이 올리는 위치, N번 칸이 내리는 위치
# 로봇은 올리는 위치에만 올릴 수 있다.
# 언제든지 내리는 위치에 도달하면 그 즉시 내린다.
# 로봇이 올려지거나 어떤 칸으로 이동하면 그 칸은 내구도 즉시 1 감소
# 내구도가 0인 칸의 개수가 K개 이상이면 종료
# 종료되었을 때 몇 단계가 진행 중이었는가


# 의문 -> 아래 벨트 왜 있는 겨??

N, K = map(int, input().split())
# 컨베이어 벨트
arr = list(map(int, input().split()))
# 로봇 - 어차피 N칸 위치에서 무조건 내리니까, N까지만 필요
robot = [0] * N
result = 0

def rotate(arr):
    new_arr = arr[-1:] + arr[:-1]
    arr = new_arr
    # print(arr)
    return arr


while True:
    # 단계 더해줌
    result += 1
    # 벨트 회전
    arr = rotate(arr)
    robot = rotate(robot)
    # print(arr)
    # print(robot)

    # 내리는 위치에 도달한 경우, 즉시 내림
    robot[-1] = 0

    # 먼저 올라간 로봇부터 진행
    for i in range(N - 2, -1, -1):
        # 로봇 이동하기. 이동하려는 칸에 로봇 x, 내구도 1이상 남아야함.
        if arr[i + 1] >= 1 and robot[i + 1] == 0 and robot[i] == 1:
            robot[i + 1] = 1
            robot[i] = 0
            arr[i + 1] -= 1
    
    # 로봇 올리기 부분
    # 올리는 위치에 내구도 0 아니면 로봇 올리기 & 내구도 감소
    if arr[0] != 0 and robot[0] != 1:
        robot[0] = 1
        arr[0] -= 1
    # 내구도 0인 칸 수가 k 이상이면 종료
    if arr.count(0) >= K:
        break
print(result)
