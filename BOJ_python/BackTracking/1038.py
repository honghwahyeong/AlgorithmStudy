n = int(input())

cnt = 10
num = 11
if n <= 10:
    print(n)
elif n > 1022:
    print(-1)
else:
    while True:
        str_num = str(num)
        flag = True
        for i in range(1, len(str_num)):
            if int(str_num[i-1]) > int(str_num[i]):
                continue
            else:
                start = str_num[:i-1]
                mid = str(int(str_num[i-1])+1)
                end = '0' + str_num[i+1:]
                num = int(start + mid + end)
                flag = False
                break
        if flag:
            cnt += 1
            if cnt == n:
                print(num)
                break
            num += 1
