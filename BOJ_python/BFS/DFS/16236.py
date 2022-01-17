from collections import deque

n = int(input())
board = []

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

baby_size = 2
size_count = 0
baby_x, baby_y = 0, 0
result = 0
for i in range(n):
    board.append(list(map(int, input().split())))

# 아기상어 위치 확인
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            board[i][j] = 0
            baby_x, baby_y = i, j
            break

while True:
    q = deque()
    q.append((baby_x, baby_y, 0))
    visited = [[False] * n for _ in range(n)]
    flag = 1e9
    fish = []
    while q:
        x, y, count = q.popleft()

        if count > flag:
            break
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if board[nx][ny] > baby_size or visited[nx][ny]:
                continue

            if board[nx][ny] != 0 and board[nx][ny] < baby_size:
                fish.append((nx, ny, count+1))
                flag = count
            visited[nx][ny] = True
            q.append((nx, ny, count+1))

    if len(fish) > 0:
        fish.sort()
        x, y, move = fish[0][0], fish[0][1], fish[0][2]
        result += move
        size_count += 1
        board[x][y] = 0
        if size_count == baby_size:
            baby_size += 1
            size_count = 0
        baby_x, baby_y = x, y
    else:
        break
print(result)
