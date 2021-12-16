import sys

n, k = map(int, sys.stdin.readline().split())

array_A = list(map(int, sys.stdin.readline().split()))
array_B = list(map(int, sys.stdin.readline().split()))

array_A.sort()
array_B.sort(reverse=True)

for i in range(k):
    if array_A[i] < array_B[i]:
        array_A[i], array_B[i] = array_B[i], array_A[i]
    else:
        break

print(sum(array_A))
