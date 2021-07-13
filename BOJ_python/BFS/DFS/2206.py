from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0][1] = 1
    while queue:
        ax, ay, az = queue.popleft()
        if ax == N-1 and ay == M-1:
            return visited[ax][ay][az]
        for j in range(4):
            nx = ax + dx[j]
            ny = ay + dy[j]
            if 0 <= nx < N and 0 <= ny < M:
                if int_board[nx][ny] == 1 and az == 1:
                    visited[nx][ny][0] = visited[ax][ay][1] + 1
                    queue.append((nx, ny, 0))
                elif int_board[nx][ny] == 0 and visited[nx][ny][az] == 0:
                    visited[nx][ny][az] = visited[ax][ay][az] + 1
                    queue.append((nx, ny, az))
    return -1


N, M = map(int, input().split())

int_board = [list(map(int, list(input().strip()))) for _ in range(N)]

visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

print(bfs())
