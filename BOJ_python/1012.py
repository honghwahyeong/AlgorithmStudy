from collections import deque

T = int(input())
for i in range(T):
    done = []
    count = 0
    row, column, n = list(map(int, input().split(' ')))
    maps = [[0]*column for _ in range(row)]
    for i in range(n):
        posX, posY = list(map(int, input().split(' ')))
        maps[posX][posY] = 1

    def BFS(x, y):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        queue = deque()
        queue.append((x, y))
        maps[x][y] = 0
        done.append((x, y))
        while queue:
            temp = queue.popleft()
            for i in range(4):
                nx = temp[0] + dx[i]
                ny = temp[1] + dy[i]
                if(0 <= nx < row) and (0 <= ny < column):
                    if maps[nx][ny] == 1 and ((nx, ny) not in done):
                        maps[nx][ny] = 0
                        queue.append((nx, ny))
                        done.append((nx, ny))

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 1:
                BFS(i, j)
                count += 1
    print(count)
