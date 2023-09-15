def bfs():

    while True:
        i, j, alphabet = q.popleft()
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = di + i, dj + j
            print(ni, nj, q)
            if 0 <= ni < R and 0 <= nj < C:
                lang = board[ni][nj]
                if lang not in alphabet:
                    print(ni, nj, alphabet)
                    alphabet += lang
                    q.append((ni, nj, alphabet))



R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
q = deque()
#  alphabet.append(board[0][0])
visited = [[0] * C for _ in range(R)]
visited[0][0] = 1
print(board)
q.append((0, 0, board[0][0]))
print(bfs())
