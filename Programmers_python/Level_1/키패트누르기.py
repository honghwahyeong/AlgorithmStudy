def solution(numbers, hand):
    keypad = [[1,2,3],
              [4,5,6],
              [7,8,9,],
              ['*',0,'#']]
    result = ""
    position = ['*','#']
    left = [0,0]
    right = [0,0]
    length = 0
    for i in numbers:
        if i==1 or i==4 or i==7:
            result += 'L'
            position[0] = i
        elif i==3 or i==6 or i==9:
            result += 'R'
            position[1] = i
        else:
            for a in range(len(keypad)):
                for b in range(len(keypad[a])):
                    if position[0] == keypad[a][b]:
                        left[0] = a
                        left[1] = b
                    if position[1] == keypad[a][b]:
                        right[0] = a
                        right[1] = b
            for a in range(len(keypad)):
                for b in range(len(keypad[a])):
                    if i == keypad[a][b]:
                        left[0] = abs(left[0]-a)
                        left[1] = abs(left[1]-b)
                        right[0] = abs(right[0]-a)
                        right[1] = abs(right[1]-b)
            length = left[0]+left[1]
            if length>right[0]+right[1]:
                result += 'R'
                position[1] = i
            elif length<right[0]+right[1]:
                result += 'L'
                position[0] = i
            else:
                if hand=='right':
                    result += 'R'
                    position[1] = i
                else:
                    result += 'L'
                    position[0] = i
    return result