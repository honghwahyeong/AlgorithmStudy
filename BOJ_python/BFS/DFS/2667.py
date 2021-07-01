from collections import deque

n = int(input())
maps = [list(input())for _ in range(n)]
done = []
result = []


def BFS(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    queue = deque()
    queue.append((x, y))
    maps[x][y] = '0'
    done.append((x, y))
    while queue:
        temp = queue.popleft()
        cnt += 1
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if(0 <= nx < n) and (0 <= ny < n):
                if maps[nx][ny] == '1' and ((nx, ny) not in done):
                    maps[nx][ny] = '0'
                    queue.append((nx, ny))
                    done.append((nx, ny))
    return cnt


for i in range(n):
    for j in range(n):
        if maps[i][j] == '1':
            result.append(BFS(i, j))
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])
