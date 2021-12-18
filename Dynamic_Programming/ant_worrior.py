import sys

n = int(sys.stdin.readline().rstrip())
k = list(map(int, sys.stdin.readline().rstrip().split()))

d = [0]*101

d[1] = k[0]
d[2] = k[1]

for i in range(3, n+1):
    d[i] = d[i-2] + k[i-1]
    if i != 3:
        d[i] = max(d[i], d[i-3]+k[i-1])

print(max(d))
