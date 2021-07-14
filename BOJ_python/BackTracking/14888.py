
def back(cnt, result, add, sub, mul, div):
    if cnt == N:
        llist.append(result)
        return
    if add:
        back(cnt+1, result+board[cnt], add-1, sub, mul, div)
    if sub:
        back(cnt+1, result-board[cnt], add, sub-1, mul, div)
    if mul:
        back(cnt+1, result*board[cnt], add, sub, mul-1, div)
    if div:
        if result < 0:
            back(cnt+1, -(-result//board[cnt]), add, sub, mul, div-1)
        else:
            back(cnt+1, result//board[cnt], add, sub, mul, div-1)


N = int(input())
board = list(map(int, input().split()))
cal = list(map(int, input().split()))
llist = []
back(1, board[0], cal[0], cal[1], cal[2], cal[3])
print(max(llist))
print(min(llist))
