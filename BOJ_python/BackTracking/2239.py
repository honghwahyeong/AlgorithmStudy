import sys
from collections import deque

input = sys.stdin.readline

board = [list(map(int, input().rstrip())) for _ in range(9)]
num_arr = [[0]*9 for _ in range(27)]

for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            num_arr[i][board[i][j]-1] = 1
            num_arr[9+j][board[i][j]-1] = 1
            num_i = i // 3
            num_j = j // 3
            num_arr[18+(3*num_i)+num_j][board[i][j]-1] = 1


def sol(n):
    if n == 81:
        for i in board:
            print(''.join(map(str, i)))
        return True
    x = n // 9
    y = n % 9
    local_x = x // 3
    local_y = y // 3
    if board[x][y] != 0:
        return sol(n+1)
    else:
        for num in range(9):
            if num_arr[x][num] == 0 and num_arr[9+y][num] == 0 and num_arr[18+(3*local_x)+local_y][num] == 0:
                board[x][y] = num+1
                num_arr[x][num] = 1
                num_arr[9+y][num] = 1
                num_arr[18+(3*local_x)+local_y][num] = 1
                if sol(n+1):
                    return True
                board[x][y] = 0
                num_arr[x][num] = 0
                num_arr[9+y][num] = 0
                num_arr[18+(3*local_x)+local_y][num] = 0
    return False


sol(0)
