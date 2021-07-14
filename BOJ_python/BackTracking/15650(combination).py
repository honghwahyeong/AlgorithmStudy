from itertools import combinations

N, M = map(int, input().split())
llist = []
for i in range(N):
    llist.append(i+1)
board = list(combinations(llist, M))
board.sort()
for i in board:
    for j in range(len(i)):
        print(i[j], end=' ')
    print()
