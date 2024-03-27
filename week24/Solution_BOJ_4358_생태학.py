# 사전 순으로 정렬한다고 heapq 썼는데 더 비효율적인듯..
# 딕셔너리도 sort가 가능하다는 사실을 잊고 있었음.
# trees_list = sorted(trees, key = lambda x: x[0]) 
# 람다식.. 사전과제로 학습해서 1학기 극초반에 활용했었는데 지금은 완전히 잊고 있었음..

import heapq

dict = {}
q = []
cnt = 0 # 총 나무 수
while True:
    try:
        type = input()
    except:
        break

    cnt += 1
    if type in dict:
        dict[type] += 1
    else:
        dict[type] = 1
        heapq.heappush(q, type)

# print(dict, q)

while q:
    type = heapq.heappop(q)
    print(f"{type}{dict[type] / cnt * 100: .4f}")
