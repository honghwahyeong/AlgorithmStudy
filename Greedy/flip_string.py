import sys

input = sys.stdin.readline

s = list(map(int, input().strip()))

count = [0, 0]
is_zero = True

count[s[0]] += 1
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i] == 0:
            count[0] += 1
        elif s[i] == 1:
            count[1] += 1
print(min(count))
