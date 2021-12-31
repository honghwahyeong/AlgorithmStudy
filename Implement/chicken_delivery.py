from itertools import combinations

n, m = map(int, input().split())
city = []
chicken_store = []

for _ in range(n):
    data = list(map(int, input().split()))
    city.append(data)

for i in range(len(city)):
    for j in range(len(city)):
        if city[i][j] == 2:
            chicken_store.append((i, j))

chicken_store_combi = list(combinations(chicken_store, m))
