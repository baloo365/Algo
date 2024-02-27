import heapq

N = int(input())
arr = list(map(int, input().split()))

heap = []
for i in arr:
    heapq.heappush(heap, i)
# print(heap)

for i in range(0, N-1):
    nums = list(map(int, input().split()))
    for num in nums:
        if heap[0] < num:
            heapq.heappush(heap, num)
            heapq.heappop(heap)

print(heap[0])
