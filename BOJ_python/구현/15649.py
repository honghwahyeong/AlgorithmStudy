N, M = map(int, input().split(' '))
visited = [False]*N
llist = []


def func(x):
    if x == M:
        for i in llist:
            print(i, end=' ')
        print()
        return
    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            llist.append(i+1)
            func(x+1)
            visited[i] = False
            llist.pop()


func(0)
