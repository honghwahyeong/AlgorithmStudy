import sys
input = sys.stdin.readline

L, C = map(int, input().split())
board = list(map(str, input().split()))
board.sort()
print(board)
isvowel = [0]*C
isnotvowel = [0]*C
sstring = ''


def dfs(idx, depth):
    global sstring
    if depth == L:
        if sum(isvowel) >= 1 and sum(isnotvowel) >= 2:
            print(sstring)
            return
        else:
            return
    for i in range(idx, C):
        if board[i] in 'aeiou':
            isvowel[i] = 1
        else:
            isnotvowel[i] = 1
        sstring += board[i]
        dfs(i+1, depth+1)
        sstring = sstring[:-1]
        if board[i] in 'aeiou':
            isvowel[i] = 0
        else:
            isnotvowel[i] = 0


dfs(0, 0)
