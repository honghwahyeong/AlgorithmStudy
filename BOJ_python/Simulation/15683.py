import copy

mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = []
cctv = []
for i in range(n):
    data = list(map(int, input().split()))
    board.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append([data[j], i, j])


def watch(boa, mm, x, y):
    for i in mm:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if boa[nx][ny] == 6:
                break
            elif boa[nx][ny] == 0:
                boa[nx][ny] = 7


def dfs(depth, arr):
    global min_val

    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += arr[i].count(0)
        min_val = min(min_val, count)
        return
    tmp = copy.deepcopy(arr)
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        watch(tmp, i, x, y)
        dfs(depth+1, tmp)
        tmp = copy.deepcopy(arr)


min_val = int(1e9)
dfs(0, board)
print(min_val)
