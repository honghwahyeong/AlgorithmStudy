N, M = map(int, input().split())
board = list(map(int, input().split()))
board.sort()
llist = []


def dfs(idx, depth):
    if depth == M:
        for i in llist:
            print(i, end=' ')
        print()
        return
    for i in range(idx, N):
        llist.append(board[i])
        dfs(i, depth+1)
        llist.pop()


dfs(0, 0)
