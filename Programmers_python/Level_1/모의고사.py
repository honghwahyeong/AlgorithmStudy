#너무 생각없이 풀이함. 맞았지만 다시 생각해봐야함.
def solution(answers):
    student1 = 0
    student2 = 0
    student3 = 0
    llist = []
    for i in range(len(answers)):
        if i%5==0:
            if answers[i]==1:
                student1 += 1
        elif i%5==1:
            if answers[i]==2:
                student1 += 1
        elif i%5==2:
            if answers[i]==3:
                student1 += 1
        elif i%5==3:
            if answers[i]==4:
                student1 += 1
        else:
            if answers[i]==5:
                student1 += 1
                
        if i%8==0:
            if answers[i]==2:
                student2 += 1
        elif i%8==1:
            if answers[i]==1:
                student2 += 1
        elif i%8==2:
            if answers[i]==2:
                student2 += 1
        elif i%8==3:
            if answers[i]==3:
                student2 += 1
        elif i%8==4:
            if answers[i]==2:
                student2 += 1
        elif i%8==5:
            if answers[i]==4:
                student2 += 1
        elif i%8==6:
            if answers[i]==2:
                student2 += 1
        else:
            if answers[i]==5:
                student2 += 1
                
        if i%10==0 or i%10==1:
            if answers[i]==3:
                student3 += 1
        if i%10==2 or i%10==3:
            if answers[i]==1:
                student3 += 1
        if i%10==4 or i%10==5:
            if answers[i]==2:
                student3 += 1
        if i%10==6 or i%10==7:
            if answers[i]==4:
                student3 += 1
        if i%10==8 or i%10==9:
            if answers[i]==5:
                student3 += 1
    max = student1
    llist.append(1)
    if student2 > max:
        llist.clear()
        llist.append(2)
        max = student2
    elif student2 == student1:
        llist.append(2)
    if student3 > max:
        llist.clear()
        llist.append(3)
    elif student3 == max:
        llist.append(3)
    return llist