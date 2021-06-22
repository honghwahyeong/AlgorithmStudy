def solution(nums):
    answer = 0
    pocketmon_num = len(set(nums))
    get_pocketmon = len(nums)/2
    if get_pocketmon > pocketmon_num:
        answer = pocketmon_num
    else:
        answer = get_pocketmon
    
    return answer