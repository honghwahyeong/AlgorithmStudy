import sys
sys.setrecursionlimit(10000)


def dfs(x, y, board=[], visited=[]):
    dx = [1, 1, 1, -1, -1, -1, 0, 0]
    dy = [0, 1, -1, 0, 1, -1, 1, -1]
    visited[x][y] = True
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == False and board[nx][ny] == 1:
                visited[nx][ny] = True
                dfs(nx, ny, board, visited)


while 1:
    m, n = map(int, input().split(' '))
    if n == 0 and m == 0:
        break
    cnt = 0
    board = [[] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        board[i] = list(map(int, input().split(' ')))
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and board[i][j] != 0:
                cnt += 1
                dfs(i, j, board, visited)
    print(cnt)
