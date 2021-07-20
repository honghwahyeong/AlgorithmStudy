
def dfs(cnt, depth):
    if depth == 6:
        for i in range(6):
            print(lucky[i], end=' ')
        print()
        return
    for i in range(cnt, len(board)):
        lucky[depth] = board[i]
        dfs(i+1, depth+1)
lucky = [0 for _ in range(13)]
while 1:
    board = list(map(int, input().split()))
    if board[0] == 0:
        break
    board = board[1:]

    dfs(0, 0)
    print()