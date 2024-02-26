import heapq

N = int(input())
heap = []
dasom = 0
for i in range(1, N+1):
    num = int(input())
    if i != 1:
        heapq.heappush(heap, -num)
    else:
        dasom = num

cnt = 0

while heap:
    max_vote = -heapq.heappop(heap)
    if max_vote < dasom:
        break
    dasom += 1
    cnt += 1
    heapq.heappush(heap, -(max_vote-1))

print(cnt)


# 다솜이는 기호 1번
# 자신을 찍지 않으려는 사람 돈으로 매수
# 다른 모든 사람의 득표수보다 많은 득표수를 가져야 함.
