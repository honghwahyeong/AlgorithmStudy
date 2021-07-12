from collections import deque
M, N, K = map(int, input().split())

board = [[0 for _ in range(N)] for _ in range(M)]

for i in range(K):
    ay, ax, by, bx = map(int, input().split())
    for j in range(ax, bx):
        for k in range(ay, by):
            board[j][k] = 1

ddx = [-1, 1, 0, 0]
ddy = [0, 0, -1, 1]
square = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            count = 1
            board[i][j] = 1
            queue = deque()
            queue.append((i, j))
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx = x + ddx[k]
                    ny = y + ddy[k]
                    if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == 0:
                        board[nx][ny] = 1
                        count += 1
                        queue.append((nx, ny))
            square.append(count)
square.sort()
print(len(square))
for i in square:
    print(i, end=' ')
