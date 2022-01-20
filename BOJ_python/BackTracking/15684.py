import sys
input = sys.stdin.readline
min_line = 4


def check():
    for i in range(1, n+1):
        cur_y = i
        for cur_x in range(1, h+1):
            if board[cur_x][cur_y] == 1:  # 지금 세로선에서 오른쪽으로 뻗은 가로선이 있으면
                cur_y += 1
            elif board[cur_x][cur_y-1] == 1:  # 지금 세로선에서 왼쪽으로 뻗은 가로선이 있으면
                cur_y -= 1
        if cur_y != i:
            return False
    return True


def sol(cnt, num):
    global min_line
    if cnt >= min_line:
        return
    if check():  # check가 True면
        min_line = cnt
        return
    for idx in range(num+1, len(candidate)):
        x, y = candidate[idx]
        if board[x][y-1] == 0 and board[x][y+1] == 0:
            board[x][y] = 1
            sol(cnt+1, idx)
            board[x][y] = 0


n, m, h = map(int, input().split())
board = [[0 for _ in range(n+1)] for _ in range(h+1)]
candidate = []
for _ in range(m):
    a, b = map(int, input().split())
    board[a][b] = 1
for i in range(1, h+1):
    for j in range(1, n):
        if board[i][j-1] == 0 and board[i][j] == 0 and board[i][j+1] == 0:
            candidate.append((i, j))

for i in board:
    print(i)

sol(0, -1)
print(min_line if min_line < 4 else -1)
