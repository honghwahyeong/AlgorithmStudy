import sys

input = sys.stdin.readline

n = int(input())
fear = list(map(int, input().split()))
group = 0
count = 0

fear.sort()

for i in fear:
    count += 1
    if count == i:
        group += 1
        count = 0

print(group)
