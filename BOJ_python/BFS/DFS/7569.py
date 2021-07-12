from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():
    while queue:
        a, b, c = queue.popleft()
        for i in range(6):
            nx = a + dx[i]
            ny = b + dy[i]
            nz = c + dz[i]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if board[nz][ny][nx] == 0:
                    queue.append((nx, ny, nz))
                    board[nz][ny][nx] = board[c][b][a] + 1


M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
max_day = 0
queue = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 1:
                queue.append((k, j, i))
bfs()
flag = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 0:
                flag = 1
            max_day = max(max_day, board[i][j][k])
if flag == 0:
    print(max_day-1)
else:
    print(-1)
