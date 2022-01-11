n, k = map(int, input().split())

graph = [[0] * 201 for _ in range(201)]

for i in range(201):
    graph[1][i] = 1
    graph[2][i] = i+1

for i in range(2, 201):
    graph[i][1] = i
    for j in range(2, 201):
        graph[i][j] = (graph[i][j-1]+graph[i-1][j]) % int(1e9)

print(graph[k][n])
