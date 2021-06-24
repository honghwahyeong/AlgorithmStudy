from itertools import combinations
def solution(nums):
    count = 0
    prime_num = 0
    llist = list(combinations(nums,3))
    for i in llist:
        for j in range(1,sum(i)+1):
            if sum(i)%j == 0:
                count += 1
            else:
                continue
        if count!=2:
            count = 0
        else:
            prime_num += 1
            count = 0
    return prime_num