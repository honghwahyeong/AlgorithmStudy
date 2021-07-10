import sys
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [0]*26
R, C = map(int, input().split())

board = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(R)]
count = 1
visited[board[0][0]] = 1


def dfs(x, y, cnt):
    global count
    count = max(cnt, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < C and 0 <= ny < R:
            if visited[board[ny][nx]] == 0:
                visited[board[ny][nx]] = 1
                dfs(nx, ny, cnt+1)
                visited[board[ny][nx]] = 0


dfs(0, 0, count)
print(count)
