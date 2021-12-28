import sys

input = sys.stdin.readline

n = int(input())
money = list(map(int, input().split()))
money.sort()

target = 1
for x in money:
    if target < x:
        break
    target += x

print(target)
