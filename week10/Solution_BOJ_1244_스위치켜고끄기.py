N = int(input())

arr = [0] + list(map(int, input().split()))
# print(arr)
student = int(input())

for _ in range(student):
    gender, s_num = map(int, input().split())  # 남:1, 여:2, 받은 수
    if gender == 1:
        for a in range(len(arr)):
            if a % s_num == 0 and a != 0:
                if arr[a] == 1:
                    arr[a] = 0
                else:
                    arr[a] = 1

    # print(arr)
    elif gender == 2:
        dj = [-1, 1]    # 왼쪽, 오른쪽
        a = 1

        if arr[s_num] == 1:
            arr[s_num] = 0
        else:
            arr[s_num] = 1

        while 1 <= s_num + dj[0]*a <= N and 1 <= s_num + dj[1]*a <= N:
            left = s_num + dj[0]*a
            right = s_num + dj[1]*a

            if arr[left] == arr[right]:
                if arr[left] == 1:
                    arr[left] = 0
                    arr[right] = 0
                else:
                    arr[left] = 1
                    arr[right] = 1
            else:
                break
            a += 1

ans = arr[1::]
for v in range(0, len(ans), 20):
    print(*ans[v:v+20])
