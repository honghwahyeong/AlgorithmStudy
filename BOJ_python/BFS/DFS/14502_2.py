from collections import deque
from itertools import combinations
import copy


def bfs(tmp, x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    queue = deque()
    queue.append((x, y))
    count = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = 2
                    queue.append((nx, ny))
                    count += 1
    return count


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

zero_board = []
virus_board = []
zero_area = 0
result = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            zero_board.append((i, j))
            zero_area += 1
        elif board[i][j] == 2:
            virus_board.append((i, j))

zero_combi = list(combinations(zero_board, 3))

for zero_set in zero_combi:
    tmp = copy.deepcopy(board)
    zero_area_tmp = zero_area
    for zero in zero_set:
        zero_x, zero_y = zero
        tmp[zero_x][zero_y] = 1
        zero_area_tmp -= 1
    for x, y in virus_board:
        zero_area_tmp -= bfs(tmp, x, y)
    result = max(result, zero_area_tmp)
print(result)
