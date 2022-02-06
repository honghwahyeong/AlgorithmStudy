t = int(input())
for _ in range(t):
    n = int(input())
    board = [0] * (n+1)
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            if board[j] == 0:
                board[j] = 1
            else:
                board[j] = 0
    print(sum(board))
