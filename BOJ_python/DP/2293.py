n, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(int(input()))

graph.sort()

llist = [0] * (k+1)
llist[0] = 1

for i in graph:
    for j in range(i, k+1):
        llist[j] += llist[j-i]

print(llist[k])
