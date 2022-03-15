
def sol(cnt, x):
    global flag
    if x > b:
        return
    elif x == b:
        print(cnt+1)
        flag = True
        return

    for i in range(2):
        if not i:
            sol(cnt+1, x*10+1)
        elif i:
            sol(cnt+1, x*2)


a, b = map(int, input().split())
flag = False
sol(0, a)
if not flag:
    print(-1)
