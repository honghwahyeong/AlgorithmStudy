N, M = map(int, input().split())

board = []


def dfs(cnt):
    if len(board) == M:
        print(' '.join(map(str, board)))
        return
    for i in range(cnt, N+1):
        if i not in board:
            board.append(i)
            dfs(i+1)
            board.pop()


dfs(1)
