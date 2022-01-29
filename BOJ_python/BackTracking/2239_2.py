import sys

input = sys.stdin.readline

board = [list(map(int, input().rstrip())) for _ in range(9)]
num_arr = [[0]*9 for _ in range(27)]
blank = []
is_done = False

for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            num_arr[i][board[i][j]-1] = 1
            num_arr[9+j][board[i][j]-1] = 1
            num_i = i // 3
            num_j = j // 3
            num_arr[18+(3*num_i)+num_j][board[i][j]-1] = 1
        else:
            blank.append((i, j))
count = 0


def sol(idx):
    global is_done, count
    if is_done:
        return

    if idx == len(blank):
        is_done = True
        for i in board:
            print(''.join(map(str, i)))
        return
    x, y = blank[idx]
    local_x = x // 3
    local_y = y // 3
    for num in range(9):
        if num_arr[x][num] == 0 and num_arr[9+y][num] == 0 and num_arr[18+(3*local_x)+local_y][num] == 0:
            board[x][y] = num+1
            num_arr[x][num] = 1
            num_arr[9+y][num] = 1
            num_arr[18+(3*local_x)+local_y][num] = 1
            sol(idx+1)
            board[x][y] = 0
            num_arr[x][num] = 0
            num_arr[9+y][num] = 0
            num_arr[18+(3*local_x)+local_y][num] = 0
    return


sol(0)
