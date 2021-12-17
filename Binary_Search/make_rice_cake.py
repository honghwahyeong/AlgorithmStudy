import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
rice_cake = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(rice_cake)

result = 0
while(start <= end):
    total = 0
    mid = (start - end)//2
    for x in rice_cake:
        if x > mid:
            total += x - mid
        if total < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

print(result)
