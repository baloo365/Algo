from collections import deque


N = int(input())
arr = deque(enumerate(list(map(int, input().split()))))

temp_list = []
while arr:
    idx, val = arr.popleft()
    temp_list.append(idx + 1)

    if val > 0:
        arr.rotate(-(val - 1))  # Rotate left (counter-clockwise)
    else:
        arr.rotate(-val)  # Rotate right (clockwise)

print(*temp_list)
