import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = list(map(int, input().split()))
board.sort()
llist = []


def dfs(depth):
    if depth == M:
        for i in llist:
            print(i, end=' ')
        print()
        return
    for i in range(N):
        llist.append(board[i])
        dfs(depth+1)
        llist.pop()


dfs(0)
