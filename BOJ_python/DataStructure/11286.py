import heapq
import sys

n = int(input())
hq = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(hq, (abs(x), x))
    else:
        if hq == []:
            print(0)
        else:
            print(heapq.heappop(hq)[1])
