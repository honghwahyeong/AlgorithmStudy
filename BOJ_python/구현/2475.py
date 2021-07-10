llist = list(map(int, input().split()))
for i in range(len(llist)):
    llist[i] = llist[i]*llist[i]
ssum = sum(llist)
print(ssum % 10)
