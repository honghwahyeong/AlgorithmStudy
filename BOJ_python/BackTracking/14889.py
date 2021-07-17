N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

for i in board:
    ssum = sum(i)


def back(idx, cnt):
    global ans
    if cnt == (N//2):
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if select[i] and select[j]:
                    start += board[i][j]
                elif not select[i] and not select[j]:
                    link += board[i][j]
        ans = min(ans, abs(start-link))

    for i in range(idx, N):
        if select[i]:
            continue
        select[i] = 1
        back(i+1, cnt+1)
        select[i] = 0


select = [0]*N
ans = 100000
back(0, 0)
print(ans)
