def solution(array, commands):
    sol = [0 for i in range(len(commands))]
    for i in range(len(commands)):
        new_array = array[commands[i][0]-1:commands[i][1]]
        new_array.sort()
        sol[i]=new_array[commands[i][2]-1]
    return sol