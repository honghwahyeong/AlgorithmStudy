n = int(input())
k = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]
data = []
for _ in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 1
l = int(input())
for _ in range(l):
    x, c = input().split()
    data.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


def simul():
    x, y = 1, 1
    graph[x][y] = 2
    direction = 0
    count = 0
    index = 0
    q = [(x, y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and graph[nx][ny] != 2:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                graph[px][py] = 0
            if graph[nx][ny] == 1:
                graph[nx][ny] = 2
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


print(simul())
