str1 = list(input())
str2 = list(input())

len_str1 = len(str1)
len_str2 = len(str2)

graph = [[0] * (len_str2+1) for _ in range(len_str1+1)]

for i in range(1, len_str1+1):
    for j in range(1, len_str2+1):
        if str1[i-1] == str2[j-1]:
            graph[i][j] = graph[i-1][j-1] + 1
        else:
            graph[i][j] = max(graph[i][j-1], graph[i-1][j])

print(graph[-1][-1])
