import sys

input = sys.stdin.readline

n, m = map(int, input().split())
pound = list(map(int, input().split()))

array = [0] * 11

for x in pound:
    array[x] += 1

result = 0

for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n

print(result)
