import sys

input = sys.stdin.readline

n, m = map(int, input().split())
pound = list(map(int, input().split()))
count = 0

pound.sort()

for i in range(len(pound)-1):
    for j in range(i+1, len(pound)):
        if pound[i] != pound[j]:
            count += 1

print(count)
