import sys

n = int(input())


def check(arr, number):
    arr += number
    for i in range(1, len(arr)//2+1):
        for j in range(i, len(arr) - i+1):
            if arr[j-i:j] == arr[j:j+i]:
                return False
    return True


def sol(cnt, num_arr):
    global board
    if cnt == n:
        print(num_arr)
        sys.exit()
    for i in range(1, 4):  # 1,2,3 한개씩 넣어보면서
        if check(num_arr, str(i)):  # check 함수로 좋은 수열이 맞으면 계속 진행
            sol(cnt+1, num_arr+str(i))


sol(1, '1')
