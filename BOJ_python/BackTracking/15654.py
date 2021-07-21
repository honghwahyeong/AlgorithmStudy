import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = list(map(int, input().split()))
board.sort()
isused = [0]*N
llist = []


def dfs(depth):
    if depth == M:
        for i in llist:
            print(i, end=' ')
        print()
        return
    for i in range(len(board)):
        if isused[i] == 0:
            isused[i] = 1
            llist.append(board[i])
            dfs(depth+1)
            isused[i] = 0
            llist.pop()


dfs(0)
