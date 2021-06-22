def solution(a, b):
    for i in range(len(a)):
        a[i]=a[i]*b[i]
    return sum(a)