from collections import deque
import sys
sys.setrecursionlimit(100000)
N = int(sys.stdin.readline())


def dfs(x, y, i):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited.append((x, y))
    queue = deque()
    queue.append((x, y))
    while queue:
        qx, qy = queue.popleft()
        for j in range(4):
            nx = qx + dx[j]
            ny = qy + dy[j]
            if 0 <= nx < N and 0 <= ny < N:
                if (nx, ny) not in visited and board[nx][ny] > i:
                    queue.append((nx, ny))
                    visited.append((nx, ny))


board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_island = 1

for i in range(max(map(max, board))):
    count = 0
    visited = []
    for a in range(N):
        for b in range(N):
            if (a, b) not in visited and board[a][b] > i:
                dfs(a, b, i)
                count += 1
    max_island = max(max_island, count)
print(max_island)
