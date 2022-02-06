t = int(input())
for _ in range(2):
    n = int(input())
    answer = 0

    for i in range(1, n+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count % 2 == 1:
            answer += 1
    print(answer)
