import sys

N, D = map(int, input().split())


def shortcut():
    global length
    global s
    global e
    distance = list(range(D+1))

    for i in range(D+1):
        distance[i] = min(distance[i], distance[i - 1] + 1)
        for s, e, length in arr:
            if e > D:
                continue
            if distance[e] > distance[s] + length:
                distance[e] = distance[s] + length
    return distance[-1]

arr = [[] for _ in range(N)]
for i in range(N):
    s, e, length = map(int, input().split())
    arr[i] = (s, e, length)


print(shortcut())
