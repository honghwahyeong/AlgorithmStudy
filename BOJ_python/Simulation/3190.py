from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input())
k = int(input())
board = [[0]*(n+1) for _ in range(n+1)]
data = []
for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1
l = int(input())
for _ in range(l):
    x, c = input().split()
    data.append((int(x), c))


def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


def sol():
    x, y = 1, 1
    board[x][y] = 2
    direction = 0
    count = 0
    index = 0
    q = deque()
    q.append((x, y))
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] != 2:
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.popleft()
                board[px][py] = 0
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))
        else:
            count += 1
            break
        x, y = nx, ny
        count += 1
        if index < l and count == data[index][0]:
            direction = turn(direction, data[index][1])
            index += 1
    return count


print(sol())
