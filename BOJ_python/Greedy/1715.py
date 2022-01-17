# heapq 사용해도 똑같이 풀 수 있다.
from queue import PriorityQueue

n = int(input())
cards = PriorityQueue(maxsize=100000)
result = 0
for i in range(n):
    cards.put(int(input()))

while cards.qsize() > 1:  # 카드 모음이 2개 이상일때(카드 모음이 1개 남을때까지)

    card_1 = cards.get()  # 가장 작은 수
    card_2 = cards.get()  # 두번째로 작은 수
    ssum = card_1+card_2
    cards.put(ssum)
    result += ssum
print(result)
