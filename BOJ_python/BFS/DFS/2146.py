from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    island[x][y] = island_count
    while q:
        x_, y_ = q.popleft()
        for i in range(4):
            nx = x_ + dx[i]
            ny = y_ + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1 and island[nx][ny] == 0:
                q.append((nx, ny))
                island[nx][ny] = island_count


def bfs2(a):
    global result
    dist = [[-1] * n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if island[i][j] == a:
                q.append((i, j))
                dist[i][j] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if island[nx][ny] > 0 and island[nx][ny] != a:
                result = min(result, dist[x][y])
            if island[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
island = [[0]*n for _ in range(n)]
island_count = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and island[i][j] == 0:
            island_count += 1
            bfs(i, j)


result = int(1e9)

for i in range(1, island_count+1):
    bfs2(i)

print(result)
