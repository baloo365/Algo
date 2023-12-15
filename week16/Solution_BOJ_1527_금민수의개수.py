import sys

# 어떤 수 사이 수들 중에 4와 7로만 이루어진 수가 몇개인지 출력

s_num, e_num = map(int, input().split())
q = [4, 7]
ans = 0
while len(q) > 1:
    minsu = q[0]
    # print(minsu)
    q.pop(0)

    if minsu <= e_num:
        if s_num <= minsu:
            ans += 1
        q.append(minsu*10+4)
        q.append(minsu*10+7)

print(ans)
