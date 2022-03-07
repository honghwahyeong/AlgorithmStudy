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


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
island = [[0]*n for _ in range(n)]
island_count = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and island[i][j] == 0:
            island_count += 1
            bfs(i, j)

island_edge = [[] for _ in range(island_count)]
print(island_edge)

for i in range(n):
    for j in range(n):
        if island[i][j] != 0:
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < n and 0 <= nj < n and island[ni][nj] == 0:
                    island_edge[island[i][j]-1].append((i, j))
                    break

for i in island_edge:
    print(i)
