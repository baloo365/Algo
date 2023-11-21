T = int(input())
for tc in range(1, T+1):
    num = int(input())
    # K가 정확히 3개의 삼각수의 합으로 표현될 수 있다면 1, 그렇지 않으면 0
    # 3개의 삼각수가 모두 달라야 할 필요는 없다.

    triple = [0]
    for i in range(1, 1001):
        triple.append(triple[-1] + i)
        if triple[-1] + i >= 1000:
            break

    # print(triple)

    result = 0
    N = len(triple)
    for i in range(1, N):
        for j in range(1, N):
            for k in range(1, N):
                if triple[i] + triple[j] + triple[k] == num:
                    result = 1
                    break
            if result == 1:
                break

        if result == 1:
            break

    print(result)
