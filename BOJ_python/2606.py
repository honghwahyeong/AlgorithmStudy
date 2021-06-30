from collections import deque


def BFS(graph, root):
    visited = []
    queue = deque([root])
    count = 0

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            count += 1
            if n in graph:
                temp = list(set(graph[n])-set(visited))
                temp.sort()
                queue += temp
    return count-1


graph = {}
edge = input()
node = input()
for i in range(int(node)):
    info = input().split(' ')
    n1, n2 = [int(i) for i in info]
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)
print(BFS(graph, 1))
