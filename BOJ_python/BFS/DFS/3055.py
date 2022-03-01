import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
board = []
count_board = [[0]*m for _ in range(n)]
for i in range(n):
    data = input().strip()
    board.append(data)
    for j in data:
        if j == 'S':
            s_x = i
            s_y = j
        elif j == 'D':
            des_x = i
            des_y = j
