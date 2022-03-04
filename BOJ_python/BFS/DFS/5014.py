from collections import deque


def bfs(x):
    q = deque()
    q.append(x)
    visited = [0] * f
    visited[x-1] = 1
    while q:
        nx = q.popleft()
        for i in range(2):
            nnx = nx + elevator[i]
            if 0 < nnx <= f and visited[nnx-1] == 0:
                floor[nnx-1] = floor[nx-1] + 1
                visited[nnx-1] = 1
                q.append(nnx)


f, s, g, u, d = map(int, input().split())
elevator = [u, -d]
floor = [-1]*f
floor[s-1] = 0
bfs(s)
print(floor[g-1] if floor[g-1] != -1 else "use the stairs")
