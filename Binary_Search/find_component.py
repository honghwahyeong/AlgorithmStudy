import sys


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2

    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


n = int(sys.stdin.readline().rstrip())
component = list(map(int, sys.stdin.readline().rstrip().split()))
component.sort()
m = int(sys.stdin.readline().rstrip())
find = list(map(int, sys.stdin.readline().rstrip().split()))

for i in find:
    result = binary_search(component, i, 0, n-1)
    if result == None:
        print('No', end=' ')
    else:
        print('yes', end=' ')
