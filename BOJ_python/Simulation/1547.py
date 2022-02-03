m = int(input())
data = [list(map(int, input().split())) for _ in range(m)]
board = [0, 1, 0, 0]
flag = False

for i in data:
    x, y = i
    board[x], board[y] = board[y], board[x]
for i in range(1, len(board)):
    if board[i] == 1:
        print(i)
        flag = True
        break
if not flag:
    print(-1)
