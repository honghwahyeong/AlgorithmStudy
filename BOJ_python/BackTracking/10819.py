import sys
input = sys.stdin.readline

N = int(input())
board = list(map(int, input().split()))
isused = [0]*N
llist = []

cnt = 0


def dfs(depth):
    global cnt
    if depth == N:
        count = 0
        for i in range(N-1):
            count += abs(llist[i] - llist[i+1])
        cnt = max(cnt, count)
        return
    for i in range(N):
        if isused[i] == 0:
            isused[i] = 1
            llist.append(board[i])
            dfs(depth+1)
            isused[i] = 0
            llist.pop()


dfs(0)
print(cnt)
