import sys
input = sys.stdin.readline

n, k = map(int, input().split())
words = []
alphabet = [0] * 26
for _ in range(n):
    word = str(input().rstrip())
    words.append(word[4:-4])

alphabet[ord('a')-ord('a')] = 1
alphabet[ord('c')-ord('a')] = 1
alphabet[ord('i')-ord('a')] = 1
alphabet[ord('n')-ord('a')] = 1
alphabet[ord('t')-ord('a')] = 1

max_count = 0


def sol(cnt, idx):
    global max_count, words
    if cnt == k:
        count = 0
        for word in words:
            flag = 0  # 읽을 수 있는 문자이면 0, 못읽으면 1
            for j in word:
                if alphabet[ord(j)-ord('a')] != 1:
                    flag = 1
                    break
            if flag == 0:
                count += 1
        max_count = max(count, max_count)
        return
    for i in range(idx+1, 26):  # a ~ z까지 돌면서
        if alphabet[i] != 1:
            alphabet[i] = 1
            sol(cnt+1, i)
            alphabet[i] = 0


if k < 5:  # anta, tica에서 이미 5개 문자 사용 따라서 5보다 작으면 안됨.
    print(0)
else:
    sol(5, -1)
    print(max_count)
