from collections import deque
import sys
N = int(sys.stdin.readline())


def dfs(x, y, i):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[x][y] = 1
    queue = deque()
    queue.append((x, y))
    while queue:
        qx, qy = queue.popleft()
        for j in range(4):
            nx = qx + dx[j]
            ny = qy + dy[j]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny]==0 and board[nx][ny] > i:
                    queue.append((nx, ny))
                    visited[nx][ny]=1


board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_island = 1

for i in range(0,101):
    count = 0
    visited = [[0]*N for _ in range(N)]
    for a in range(N):
        for b in range(N):
            if visited[a][b]==0 and board[a][b] > i:
                dfs(a, b, i)
                count += 1
    if count==0:
        break
    max_island = max(max_island, count)
print(max_island)
