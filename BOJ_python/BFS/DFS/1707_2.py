import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

k = int(input())


def dfs(vert, group):
    ch[vert] = group
    for i in li[vert]:
        if ch[i] == 0:
            if dfs(i, -group) is False:
                return False
        elif ch[i] == ch[vert]:
            return False
    return True


while k:
    k -= 1
    v, e = map(int, input().split())
    li = [[] for _ in range(v+1)]
    ch = [0]*(v+1)

    for i in range(e):
        a, b = map(int, input().split())
        li[a].append(b)
        li[b].append(a)

    ans = True
    for i in range(1, v+1):
        if ch[i] == 0:
            if dfs(i, 1) is False:
                ans = False
                break
    print("YES" if ans else "NO")
