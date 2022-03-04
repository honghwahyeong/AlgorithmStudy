from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

x, y = map(int, input().split())
data = [list(input()) for _ in range(x)]
land = []
for i in range(x):
    for j in range(y):
        if data[i][j] == 'L':
            land.append((i, j))

result = 0

for piece in land:
    p_x, p_y = piece
    is_visited = [[False]*y for _ in range(x)]
    is_visited[p_x][p_y] = True
    count_hour = [[-1]*y for _ in range(x)]
    count_hour[p_x][p_y] = 0
    tmp_result = 0

    q = deque()
    q.append((p_x, p_y))
    while q:
        tmp_x, tmp_y = q.popleft()
        for i in range(4):
            nx = tmp_x + dx[i]
            ny = tmp_y + dy[i]
            if 0 <= nx < x and 0 <= ny < y and data[nx][ny] == 'L' and is_visited[nx][ny] == False:
                q.append((nx, ny))
                is_visited[nx][ny] = True
                count_hour[nx][ny] = count_hour[tmp_x][tmp_y] + 1
                tmp_result = count_hour[nx][ny]

    result = max(tmp_result, result)
print(result)
