from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())

board = list(map(int, input().split()))
#permu = list(permutations(board, len(board)))
cnt = 0
for permu in permutations(board, len(board)):
    count = 0
    for i in range(len(permu)-1):
        count += abs(permu[i]-permu[i+1])
    cnt = max(cnt, count)
print(cnt)
