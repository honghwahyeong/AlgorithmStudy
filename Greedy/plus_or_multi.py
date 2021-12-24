import sys

input = sys.stdin.readline

num = list(map(int, input().strip()))
result = 0

for i in num:
    if i == 0 or result == 0:
        result += i
    else:
        result *= i

print(result)
