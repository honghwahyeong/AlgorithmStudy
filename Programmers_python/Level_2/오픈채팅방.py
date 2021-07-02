def solution(record):
    save = {}
    answer = []
    for i in record:
        i = i.split(' ')
        if i[0]== "Enter":
            save[i[1]] = i[2]
        elif i[0]=='Change':
            save[i[1]] = i[2]
    for i in record:
        i = i.split(' ')
        if i[0] == "Enter":
            answer.append(save[i[1]]+"님이 들어왔습니다.")
        elif i[0] == 'Leave':
            answer.append(save[i[1]]+"님이 나갔습니다.")
    return answer