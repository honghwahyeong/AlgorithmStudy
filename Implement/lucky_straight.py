import sys

input = sys.stdin.readline

n = list(map(int, input().strip()))


n_1 = n[0:len(n)//2]
n_2 = n[len(n)//2:]

if sum(n_1) == sum(n_2):
    print("LUCKY")
else:
    print("READY")
