from itertools import combinations


n, m = map(int, input().split())
city = []
chicken_store = []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            city.append((i, j))
        elif data[j] == 2:
            chicken_store.append((i, j))

chicken_store_combi = list(combinations(chicken_store, m))

shortest = int(1e9)

for store_set in chicken_store_combi:
    ssum = 0
    for house_x, house_y in city:
        temp = int(1e9)
        for chicken_x, chicken_y in store_set:
            temp = min(temp, abs(house_x - chicken_x)+abs(house_y - chicken_y))
        ssum += temp
    shortest = min(ssum, shortest)

print(shortest)
