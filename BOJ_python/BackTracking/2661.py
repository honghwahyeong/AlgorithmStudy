# n = int(input())
# board = []

# def check(arr,number):
#     arr += number
#     for i in range(2,len(arr)//2+1):
#         for k in range()
#         for j in range(i,len(arr),i):
#             if arr[:j]


# def sol(cnt,num_arr):
#     global board
#     if cnt == n:
#         board.append(int(num_arr))
#         return
#     for i in range(1,4): # 1,2,3 한개씩 넣어보면서
#         if check: # check 함수로 좋은 수열이 맞으면 계속 진행
#             sol(cnt+1,num_arr+str(i))


# sol(1,'1')
# board_int = list(map(int, board))
# board_int.sort()
# print(board_int[0])

n = int(input())
board = []


def sol(idx):
    global board
    for i in range(1, (idx//2)+1):
        if board[-i:] == board[-2*i:-i]:
            return -1

        if idx == n:
            for i in range(n):
                print(board[i], end='')
            return 0

        for i in range(1, 4):
            board.append(i)
            if sol(idx+1) == 0:
                return 0
            board.pop()


sol(0)
