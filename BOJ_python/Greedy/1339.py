n = int(input())
board = []
alpha = [0] * 26
result = 0

for _ in range(n):
    board.append(list(input()))

for string in board:
    for i in range(len(string)):
        alpha[ord(string[i])-ord('A')] += 10**(len(string)-1-i)

alpha.sort(reverse=True)

for i in range(10):
    if alpha[i] == 0:
        break
    else:
        result += (9-i)*alpha[i]

print(result)