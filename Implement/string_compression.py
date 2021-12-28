def solution(s):
    answer = len(s)

    for i in range(1, len(s)//2+1):
        compressed = ""
        prev = s[0:i]
        count = 1
        for j in range(i, len(s), i):
            if prev == s[j:j+i]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+i]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer
