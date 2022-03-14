from collections import deque
from copy import deepcopy

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    is_air[i][j] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < col and 0 <= ny < row and board[nx][ny] == 0 and not is_air[nx][ny]:
                is_air[nx][ny] = True
                q.append((nx, ny))


col, row = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(col)]
hour = 0
cheese = 0
for i in range(col):
    cheese += sum(board[i])

while True:
    tmp_board = deepcopy(board)
    is_air = [[False] * row for _ in range(col)]
    cheese_flag = False
    bfs(0, 0)
    for air in is_air:
        for i in air:
            if not i:
                cheese_flag = True
    if not cheese_flag:
        break
    tmp_cheese = 0
    for i in range(col):
        for j in range(row):
            if tmp_board[i][j] == 1:
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if is_air[ni][nj]:
                        tmp_board[i][j] = 0
                        break
        tmp_cheese += sum(tmp_board[i])
    hour += 1
    if not tmp_cheese:
        pass
    else:
        cheese = tmp_cheese
    board = deepcopy(tmp_board)

print(hour)
print(cheese)
