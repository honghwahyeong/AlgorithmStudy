import sys
from collections import defaultdict
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split(' '))
graph = defaultdict(list)
visited = [False]*(N + 1)
count = 0

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split(' '))
    if u not in graph:
        graph[u] = [v]
    elif v not in graph[u]:
        graph[u].append(v)
    if v not in graph:
        graph[v] = [u]
    elif u not in graph[v]:
        graph[v].append(u)


def dfs(x, graph={}, visited=[]):
    visited[x] = True
    for i in graph[x]:
        if visited[i] == False:
            dfs(i, graph, visited)


for i in range(1, N + 1):
    if visited[i] == False:
        count += 1
        dfs(i, graph, visited)
print(count)
