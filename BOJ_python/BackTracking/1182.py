import sys
input = sys.stdin.readline
N, S = map(int, input().split())

board = list(map(int, input().split()))
count = 0


def dfs(idx, ssum):
    global count
    if idx >= N:
        return
    if ssum + board[idx] == S:
        count += 1
    dfs(idx+1, ssum)
    dfs(idx+1, ssum+board[idx])


dfs(0, 0)
print(count)
