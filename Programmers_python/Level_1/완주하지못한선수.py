def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = []
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer.append(participant[i])
            break
        else:
            continue
    if len(answer) == 0:
        answer.append(participant[len(participant)-1])
    return answer[0]