str1 = list(input())
str2 = list(input())

len_str1 = len(str1)
len_str2 = len(str2)
board = [0] * len_str1

for i in range(len_str2):
    cnt = 0
    for j in range(len_str1):
        if cnt < board[j]:
            cnt = board[j]
        elif str2[i] == str1[j]:
            board[j] = cnt + 1

print(max(board))
