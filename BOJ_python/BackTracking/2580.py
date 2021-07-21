import sys
input = sys.stdin.readline


def horizon(x, val):
    if val in board[x]:
        return False
    return True


def vertical(y, val):
    for i in range(9):
        if val == board[i][y]:
            return False
    return True


def square(x, y, val):
    nx = x//3 * 3
    ny = y//3 * 3
    for i in range(3):
        for j in range(3):
            if val == board[nx+i][ny+j]:
                return False
    return True


def dfs(idx):
    if idx == len(llist):
        for i in board:
            for j in i:
                print(j, end=' ')
            print()
        sys.exit(0)
    else:
        for i in range(1, 10):
            nx = llist[idx][0]
            ny = llist[idx][1]

            if horizon(nx, i) and vertical(ny, i) and square(nx, ny, i):
                board[nx][ny] = i
                dfs(idx+1)
                board[nx][ny] = 0


board = [list(map(int, input().split())) for _ in range(9)]
llist = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
dfs(0)
