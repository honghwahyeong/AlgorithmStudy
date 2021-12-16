import sys

n = int(sys.stdin.readline())

data = []

for i in range(n):
    input_data = sys.stdin.readline().split()
    data.append((input_data[0], int(input_data[1])))

data.sort(key=lambda x: x[1])

for i in data:
    print(i[0], end=' ')
