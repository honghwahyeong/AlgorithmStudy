from itertools import permutations

n = int(input())
board = [i+1 for i in range(n)]

combi = list(permutations(board, n))
for combination in combi:
    for i in combination:
        print(i, end=' ')
    print()
