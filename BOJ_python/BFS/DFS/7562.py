from collections import deque
import copy
N = int(input())

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

for k in range(N):
    I = int(input())
    board = [[0 for _ in range(I)] for _ in range(I)]
    visited = copy.deepcopy(board)
    first_x, first_y = map(int, input().split())
    des_x, dex_y = map(int, input().split())
    visited[first_x][first_y] = 1
    queue = deque()
    queue.append((first_x, first_y))
    while queue:
        x, y = queue.popleft()
        if x == des_x and y == dex_y:
            print(board[x][y])
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < I and 0 <= ny < I:
                if board[nx][ny] == 0 and visited[nx][ny] == 0:
                    board[nx][ny] = board[x][y] + 1
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
