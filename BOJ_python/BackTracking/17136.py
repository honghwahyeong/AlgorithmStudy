import sys

input = sys.stdin.readline


def sol(y, x, cnt):
    global ans
    if y >= 10:
        ans = min(ans, cnt)
        return
    if x >= 10:
        sol(y+1, 0, cnt)
        return

    if board[y][x] == 1:
        for k in range(5):
            if colored_paper[k] == 5:
                continue
            if x+k >= 10 or y+k >= 10:
                continue

            flag = True
            for i in range(y, y+k+1):
                for j in range(x, x+k+1):
                    if board[i][j] == 0:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                for i in range(y, y+k+1):
                    for j in range(x, x+k+1):
                        board[i][j] = 0

                colored_paper[k] += 1
                sol(y, x+k+1, cnt+1)
                colored_paper[k] -= 1

                for i in range(y, y+k+1):
                    for j in range(x, x+k+1):
                        board[i][j] = 1
    else:
        sol(y, x+1, cnt)


board = [list(map(int, input().split())) for _ in range(10)]
colored_paper = [0] * 5
ans = 26
sol(0, 0, 0)
print(ans if ans != 26 else -1)
