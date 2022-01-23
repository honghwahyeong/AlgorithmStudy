n, m = map(int, input().split())
board = list(map(int, input().split()))
new_board = []

for i in board:
    if i not in new_board:
        new_board.append(i)

new_board.sort()

combi_list = []


def sol(cnt):
    if cnt == m:
        print(' '.join(map(str, combi_list)))
        return

    for i in new_board:
        combi_list.append(i)
        sol(cnt+1)
        combi_list.pop()


sol(0)
