import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        que_x, que_y = queue.popleft()
        for i in range(4):
            nx = que_x + dx[i]
            ny = que_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[que_x][que_y] + 1
                    queue.append((nx, ny))


bfs(0, 0)

print(graph[n-1][m-1])
