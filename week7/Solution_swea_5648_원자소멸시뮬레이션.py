import sys

T = int(input())

direction = ((0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0))

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    ans = 0
    while len(arr) >= 2:
        # arr 에 있는 원소들 각각의 방향으로 0.5씩 이동시킴.
        for i in range(len(arr)):
            # x좌표
            arr[i][0] += direction[arr[i][2]][0]
            # y좌표
            arr[i][1] += direction[arr[i][2]][1]

        ddel, visit = set(), set()

        # 충돌하는 원소가 있는지 확인
        for i in range(len(arr)):
            ni, nj = arr[i][1], arr[i][0]
            if (ni, nj) in visit:
                ddel.add((ni, nj))
            visit.add((ni, nj))

        for i in range(len(arr)-1, -1, -1):
            if (arr[i][1], arr[i][0]) in ddel:
                ans += arr[i][3]
                arr.pop(i)

                # print(len(arr))
      
        # 범위가 벗어나면 arr에서 제외시킴
        for i in range(len(arr)-1, -1, -1):
            # print(arr[i][1], arr[i][0])
            if (-1000 > arr[i][1] or arr[i][1] > 1000) or (-1000 > arr[i][0] or arr[i][0] > 1000):
                arr.pop(i)

        # print(len(arr))
    print(f'#{tc} {ans}')
