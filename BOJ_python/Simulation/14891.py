def sol(n, d):
    is_rotate = [False] * 4
    direction = [0] * 4
    is_rotate[n] = True
    direction[n] = d
    tmp_n = n
    tmp_d = d
    for i in range(n+1, 4):
        if wheel[tmp_n][2] != wheel[i][6]:
            is_rotate[i] = True
            tmp_d = -tmp_d
            direction[i] = tmp_d
            tmp_n = i
        else:
            break
    tmp_n = n
    tmp_d = d
    for i in range(n-1, -1, -1):
        if wheel[tmp_n][6] != wheel[i][2]:
            is_rotate[i] = True
            tmp_d = -tmp_d
            direction[i] = tmp_d
            tmp_n = i
        else:
            break
    for i in range(4):
        if is_rotate[i]:
            if direction[i] == 1:
                tmp = wheel[i].pop()
                wheel[i] = [tmp] + wheel[i]
            else:
                tmp = wheel[i][0]
                del wheel[i][0]
                wheel[i].append(tmp)


wheel = []
rotate = []
for i in range(4):
    a = list(map(int, input()))
    wheel.append(a)
k = int(input())
for i in range(k):
    a, b = map(int, input().split())
    rotate.append([a-1, b])
for n, d in rotate:
    sol(n, d)
result = 0
for i in range(4):
    if wheel[i][0] == 1:
        result += 2**i
print(result)
