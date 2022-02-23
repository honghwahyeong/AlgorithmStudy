from copy import deepcopy
from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        xx, yy = q.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if 0 <= nx < n and 0 < ny < m:
                if board[nx][ny] != 0 and is_divided[nx][ny] == 0:
                    is_divided[nx][ny] = 1
                    q.append((nx, ny))


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
count = 0

while True:
    flag = 0
    is_divided = [[0]*m for _ in range(n)]
    # 빙산확인
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and is_divided[i][j] == 0:
                is_divided[i][j] = 1
                bfs(i, j)
                flag += 1
    if flag == 0:
        print(0)
        break
    elif flag > 1:
        print(count)
        break

    glacier = []

    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                glacier.append((i, j))

    tmp_board = deepcopy(board)

    for glacier_piece in glacier:
        x, y = glacier_piece
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if board[nx][ny] == 0:
                sea += 1
        tmp_board[x][y] -= sea
        if tmp_board[x][y] <= 0:
            tmp_board[x][y] = 0
    board = tmp_board
    count += 1
