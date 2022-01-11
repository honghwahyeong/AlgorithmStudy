import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
monetary = []

for i in range(n):
    monetary.append(sys.stdin.readline().rstrip())

monetary.sort()

d = [10001] * (m+1)

for i in range(n):
    for j in range(monetary[i], m+1):
        if d[j-monetary[i]] != 10001:
            d[j] = min(d[j], d[j-monetary[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
