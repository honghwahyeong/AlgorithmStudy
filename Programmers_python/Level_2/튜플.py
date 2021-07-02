def solution(s):
    save = {}
    answer = []
    s = s[1:-2]
    s = s.split('},')
    for i in s:
        i = i.split('{')
        j = list(map(int, i[1].split(',')))
        for k in j:
            if k not in save:
                save[k] = 1
            else:
                save[k] += 1
    new_dict = sorted(save.items(), key=lambda x: x[1], reverse=True)
    for k, v in new_dict:
        answer.append(k)
    return answer
