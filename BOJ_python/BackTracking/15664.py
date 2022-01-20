n, m = map(int, input().split())
board = list(map(int, input().split()))
board.sort()
board_check = [0] * len(board)
num = []
dictionary = []


def sol(cnt, idx):
    global dictionary, num
    if cnt == m:
        num.sort()
        s = ' '.join(map(str, num))
        if s in dictionary:
            return
        else:
            dictionary.append(s)
            print(s)
            return

    for i in range(idx+1, len(board)):
        num.append(board[i])
        sol(cnt+1, i)
        num.pop()


sol(0, -1)
