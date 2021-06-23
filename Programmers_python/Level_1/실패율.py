#더 간결한 풀이를 생각해 봅시다.
def solution(N, stages):
    player = len(stages)
    each_stage_player = [0]*(N)
    lose_percent = {}
    llist = []
    for i in stages:
        if i==N+1:
            continue
        else:
            each_stage_player[i-1] += 1
    for i in range(len(each_stage_player)):
        if each_stage_player[i]==0:
            lose_percent[i+1] = 0
        else:
            lose_percent[i+1] = each_stage_player[i]/player
            player -= each_stage_player[i]
    lose_percent = sorted(lose_percent.items(),reverse=True, key= lambda x : x[1])
    for i in lose_percent:
        llist.append(i[0])
    return llist