import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
minsum = sys.maxsize


def dfs(start, next, cost, isvisited):
    global minsum
    if len(isvisited) == N:
        if board[next][start] != 0:
            minsum = min(minsum, cost+board[next][start])
        return
    for i in range(N):
        if board[next][i] != 0 and i != start and i not in isvisited:
            isvisited.append(i)
            cost += board[next][i]
            dfs(start, i, cost, isvisited)
            cost -= board[next][i]
            isvisited.pop()


dfs(0, 0, 0, [0])
print(minsum)
