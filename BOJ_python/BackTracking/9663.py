N = int(input())

row = [0 for _ in range(N)]
left = [0 for _ in range(2*N-1)]
right = [0 for _ in range(2*N-1)]

cnt = 0


def back(x):
    global cnt
    if x == N:
        cnt += 1
        return
    for i in range(N):
        if row[i] != 0 or left[x+i] != 0 or right[N-1+x-i] != 0:
            pass
        else:
            row[i] = left[x+i] = right[N-1+x-i] = 1
            back(x+1)
            row[i] = left[x+i] = right[N-1+x-i] = 0


back(0)
print(cnt)
