dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if board[x][y] != -1:
        return board[x][y]
    board[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if data[nx][ny] < data[x][y]:
                board[x][y] += dfs(nx, ny)
    return board[x][y]


m, n = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(m)]
board = [[-1]*n for _ in range(m)]

print(dfs(0, 0))
