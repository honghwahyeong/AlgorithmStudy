from collections import deque

case = int(input())
for _ in range(case):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    target_index = m
    count = 0
    while q:
        flag = True
        x = q.popleft()
        for i in q:
            if x < i:
                flag = False
                break
        if not flag:
            q.append(x)
            if target_index != 0:
                target_index -= 1
            else:
                target_index = len(q)-1
        else:
            if target_index == 0:
                print(count+1)
                break
            else:
                count += 1
                target_index -= 1
