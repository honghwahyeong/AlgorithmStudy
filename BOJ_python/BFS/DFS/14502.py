from itertools import combinations
from collections import deque


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = -1

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0 and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = -1


N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

empty_space = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            empty_space.append((i, j))

block = list(combinations(empty_space, 3))
max_cnt = 0
for i in range(len(block)):
    visited = [[0]*M for _ in range(N)]
    for j in block[i]:
        n, m = map(int, j)
        board[n][m] = 1
    for j in range(N):
        for k in range(M):
            visited[j][k] = board[j][k]
    for j in range(N):
        for k in range(M):
            if board[j][k] == 2:
                bfs(j, k)
    cnt = 0
    for j in range(N):
        for k in range(M):
            if visited[j][k] == 0:
                cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
    for j in block[i]:
        n, m = map(int, j)
        board[n][m] = 0
print(max_cnt)
