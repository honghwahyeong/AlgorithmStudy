from collections import deque
import sys
input = sys.stdin.readline


def bfs(i, j):
    q = deque()
    q.append([i, j])
    temp = []
    temp.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not is_visited[nx][ny]:
                if l <= abs(board[nx][ny] - board[x][y]) <= r:
                    is_visited[nx][ny] = True
                    q.append([nx, ny])
                    temp.append([nx, ny])
    return temp


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
while True:
    is_visited = [[False] * n for _ in range(n)]
    is_True = False
    for i in range(n):
        for j in range(n):
            if not is_visited[i][j]:
                is_visited[i][j] = True
                temp = bfs(i, j)
                if len(temp) > 1:
                    is_True = True
                    num = sum([board[x][y] for x, y in temp]) // len(temp)
                    for x, y in temp:
                        board[x][y] = num
    if not is_True:
        break
    cnt += 1
print(cnt)
