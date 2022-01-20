n, m = map(int, input().split())
board = list(map(int, input().split()))
new_board = []
num = []

for i in board:
    if i not in new_board:
        new_board.append(i)
new_board.sort()


def sol(cnt):
    global num
    if cnt == m:
        for i in num:
            print(i, end=' ')
        print()
        return

    for i in range(len(new_board)):
        if cnt == 0 or num[-1] <= new_board[i]:
            num.append(new_board[i])
            sol(cnt+1)
            num.pop()


sol(0)
