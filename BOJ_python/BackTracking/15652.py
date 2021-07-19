N, M = map(int, input().split())

board = []


def dfs(cnt):
    if len(board) == M:
        print(' '.join(map(str, board)))
        return
    for i in range(cnt, N+1):
        board.append(i)
        dfs(i)
        board.pop()


dfs(1)
