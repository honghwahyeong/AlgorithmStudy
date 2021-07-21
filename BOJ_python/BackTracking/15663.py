import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = list(map(int, input().split()))
board.sort()
llist = []
isused = [0]*N
isdone = {}
graph = {}


def dfs(depth):
    if depth == M:
        s = ' '.join(map(str, llist))
        if s not in isdone:
            isdone[s] = 1
            print(s)
        return

    for i in range(N):
        if isused[i] == 0:
            llist.append(board[i])
            isused[i] = 1
            dfs(depth+1)
            llist.pop()
            isused[i] = 0


dfs(0)
