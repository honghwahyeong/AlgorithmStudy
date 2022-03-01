n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1

for i in data:
    if target < i:
        break
    target += i
print(target)
# 정렬 후 하나씩 더하면서 해당 수를 arr 다음 요소(추)와 비교한다.
# 다음 추가 여태 더했던 추들의 합보다 더 크다면 해당 값은 주어진 N개의 추들로 만들 수 없다
