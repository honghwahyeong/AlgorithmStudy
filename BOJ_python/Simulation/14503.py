from collections import deque

dx = [-1, 0, 1, 0]  # 북 동 남 서
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
is_visited = [[0]*m for _ in range(n)]
is_visited[r][c] = 1
count = 1
q = deque()
q.append((r, c, d))
while 1:
    flag = False
    for _ in range(4):
        nx = r + dx[(d+3) % 4]
        ny = c + dy[(d+3) % 4]
        d = (d+3) % 4
        if 0 <= nx < n and 0 <= ny < m:
            if is_visited[nx][ny] == 0 and board[nx][ny] == 0:
                is_visited[nx][ny] = 1
                count += 1
                r = nx
                c = ny
                if not flag:
                    flag = True
                break
    if not flag:
        if 0 <= nx < n and 0 <= ny < m:
            if board[r-dx[d]][c-dy[d]] == 1:
                print(count)
                break
            else:
                r, c = r-dx[d], c-dy[d]
