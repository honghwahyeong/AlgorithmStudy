import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = []
num_count = [0]*(2*(10**9)+1)
for i in range(n):
    x = int(input())
    data.append(x)
data.sort()
print(data)
