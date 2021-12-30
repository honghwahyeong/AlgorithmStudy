def check(answer):
    for x, y, a in answer:
        if a == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        else:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        if b == 0:  # 삭제
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])
        if b == 1:  # 설치
            answer.append([x, y, a])
            if not check(answer):
                answer.remove([x, y, a])
    return sorted(answer)
