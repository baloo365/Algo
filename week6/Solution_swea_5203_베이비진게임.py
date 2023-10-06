def check_baby_gin(p):  # 베이비진 판별
    for i in p:
        if p.count(i) >= 3:  # 동일 수 3개
            return True
 
    p.sort()
    for a in range(len(p)-2):
        if (p[a] in p) and (p[a] + 1 in p) and (p[a] + 2 in p):
            return True
 
    return False
 
 
T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    N = len(card)
    p1 = []
    p2 = []
    winner = 0
 
    for i in range(N):
        if i % 2 == 0:  # 짝수일 때
            p1.append(card[i])
            if len(p1) >= 3 and check_baby_gin(p1):
                winner = 1
                break
 
        else:   # 홀수일 때
            p2.append(card[i])
            if len(p2) >= 3 and check_baby_gin(p2):
                winner = 2
                break
 
    print(f'#{tc} {winner}')
