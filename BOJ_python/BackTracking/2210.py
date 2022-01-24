board = []
for i in range(5):
    board.append(list(map(int, input().split())))


result = 0
six_num = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def sol(i, j, cnt, num_arr):
    global result
    if cnt == 6:
        if num_arr in six_num:
            return
        else:
            six_num.append(num_arr)
            result += 1
            return
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < 5 and 0 <= ny < 5:
            sol(nx, ny, cnt+1, num_arr+str(board[nx][ny]))


for i in range(5):
    for j in range(5):
        sol(i, j, 1, str(board[i][j]))

print(result)
