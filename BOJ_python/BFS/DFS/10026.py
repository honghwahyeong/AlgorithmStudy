from collections import deque
N = int(input())

board = [input() for _ in range(N)]

normal = [[0 for _ in range(N)] for _ in range(N)]
green_red = [[0 for _ in range(N)] for _ in range(N)]

normal_vis = [[0 for _ in range(N)] for _ in range(N)]
green_red_vis = [[0 for _ in range(N)] for _ in range(N)]
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 'R':
            normal[i][j] = 0
            green_red[i][j] = 0
        elif board[i][j] == 'B':
            normal[i][j] = 1
            green_red[i][j] = 1
        elif board[i][j] == 'G':
            normal[i][j] = 2
            green_red[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = [0, 0]

for i in range(N):
    for j in range(N):
        if normal[i][j] == 0 and normal_vis[i][j] == 0:
            cnt[0] += 1
            queue = deque()
            queue.append((i, j))
            normal_vis[i][j] = 1

            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if normal[nx][ny] == 0 and normal_vis[nx][ny] == 0:
                            queue.append((nx, ny))
                            normal_vis[nx][ny] = 1
        elif normal[i][j] == 1 and normal_vis[i][j] == 0:
            cnt[0] += 1
            queue = deque()
            queue.append((i, j))
            normal_vis[i][j] = 1
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if normal[nx][ny] == 1 and normal_vis[nx][ny] == 0:
                            queue.append((nx, ny))
                            normal_vis[nx][ny] = 1
        elif normal[i][j] == 2 and normal_vis[i][j] == 0:
            cnt[0] += 1
            queue = deque()
            queue.append((i, j))
            normal_vis[i][j] = 1
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if normal[nx][ny] == 2 and normal_vis[nx][ny] == 0:
                            queue.append((nx, ny))
                            normal_vis[nx][ny] = 1

        if green_red[i][j] == 0 and green_red_vis[i][j] == 0:
            cnt[1] += 1
            queue = deque()
            queue.append((i, j))
            green_red_vis[i][j] = 1
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if green_red[nx][ny] == 0 and green_red_vis[nx][ny] == 0:
                            queue.append((nx, ny))
                            green_red_vis[nx][ny] = 1
        elif green_red[i][j] == 1 and green_red_vis[i][j] == 0:
            cnt[1] += 1
            queue = deque()
            queue.append((i, j))
            green_red_vis[i][j] = 1
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if green_red[nx][ny] == 1 and green_red_vis[nx][ny] == 0:
                            queue.append((nx, ny))
                            green_red_vis[nx][ny] = 1
for i in cnt:
    print(i, end=' ')
