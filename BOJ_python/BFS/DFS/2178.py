from collections import deque

N, M = list(map(int, input().split(' ')))
maps = [list(map(int, input())) for _ in range(N)]
done = []


def BFS(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append((x, y))
    done.append((x, y))
    while queue:
        temp = queue.popleft()
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if(0 <= nx < N) and (0 <= ny < M):
                if maps[nx][ny] == 1 and ((nx, ny) not in done):
                    if nx == N-1 and ny == M-1:
                        return maps[temp[0]][temp[1]]+1
                    else:
                        queue.append((nx, ny))
                        done.append((nx, ny))
                        maps[nx][ny] = maps[temp[0]][temp[1]] + 1


print(BFS(0, 0))
