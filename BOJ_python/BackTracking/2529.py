n = int(input())
sign = list(map(str, input().split()))
num_list = [0] * 10
mx, mn = "", ""


def check(i, j, k):
    if k == ">":
        return i > j
    else:
        return i < j


def sol(cnt, s):
    global mx, mn
    if cnt > n:
        if len(mn) == 0:
            mn = s
        else:
            mx = s
        return
    for i in range(10):
        if num_list[i] == 0:
            if cnt == 0 or check(s[-1], str(i), sign[cnt-1]):
                num_list[i] = 1
                sol(cnt+1, s+str(i))
                num_list[i] = 0


sol(0, "")
print(mx)
print(mn)
