N, M = map(int, input().split())

board = []


def dfs(cnt):
    if cnt == M:
        print(' '.join(map(str, board)))
        return

    for i in range(1, N+1):
        board.append(i)
        dfs(cnt+1)
        board.pop()


dfs(0)
