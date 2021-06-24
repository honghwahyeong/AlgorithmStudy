def solution(board, moves):
    count = 0
    result = []
    for i in moves:
        for j in board:
            if j[i-1] != 0:
                if len(result) == 0:
                    result.append(j[i-1])
                else:
                    if j[i-1] == result[-1]:
                        result.pop()
                        count += 2
                    else:
                        result.append(j[i-1])
                j[i-1] = 0
                break
    return count