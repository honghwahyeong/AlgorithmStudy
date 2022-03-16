string = list(input())
pos = len(string)
m = int(input())
for i in range(m):
    x = input()
    if x == "L":
        if pos == 0:
            continue
        pos -= 1
    elif x == "D":
        if pos == len(string):
            continue
        pos += 1
    elif x == "B":
        if pos == 0:
            continue
        string.pop(pos)
    else:
        string.insert(pos, x[2])
        pos += 1

print(string)
