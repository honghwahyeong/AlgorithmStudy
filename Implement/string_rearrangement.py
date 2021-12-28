import sys

input = sys.stdin.readline

s = list(map(str, input().strip()))
ssum = 0
s.sort()

for i in s:
    if 48 <= ord(i) <= 57:
        ssum += int(i)
    else:
        print(i, end='')
if ssum != 0:
    print(ssum)
