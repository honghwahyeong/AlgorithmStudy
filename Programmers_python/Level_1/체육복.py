def solution(n, lost, reserve):
    count = n-len(lost)
    for i in reversed(lost):
        if i in reserve:
            count = count + 1
            lost.remove(i)
            reserve.remove(i)
    for i in lost:
        if i-1 in reserve:
            count = count + 1
            reserve.remove(i-1)
        elif i+1 in reserve:
            count = count + 1
            reserve.remove(i+1)
    return count