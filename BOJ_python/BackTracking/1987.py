from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, input().split())
board = []
billboard = [[0 for _ in range(C)] for _ in range(R)]
for i in range(R):
    s = input().rstrip()
    llist = []
    for i in range(len(s)):
        llist.append(ord(s[i])-ord('A'))
    board.append(llist)
alpha = [0]*26
cnt = 1
billboard[0][0] = 1


def bfs(x, y):
    global cnt
    alpha[board[x][y]] = 1
    cnt = max(cnt, billboard[x][y])
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if alpha[board[nx][ny]] == 0:
                billboard[nx][ny] = billboard[x][y]+1
                bfs(nx, ny)
    alpha[board[x][y]] = 0


bfs(0, 0)

print(cnt)
