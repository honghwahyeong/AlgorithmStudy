import sys

input = sys.stdin.readline

n = int(input())
money = list(map(int, input().split()))
length = len(money)

ssum = [0] * (500501)

for i in range(1 << length):
    hap = 0
    for j in range(length):
        if i & (1 << j):
            hap += money[j]
    ssum[hap] += 1

for i in range(1, len(ssum)):
    if ssum[i] == 0:
        print(i)
        break
