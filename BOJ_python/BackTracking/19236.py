def move_fish():

    # 북 북서 서  남서 남  남동 동  북동
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

data = [list(map(int, input().split())) for _ in range(4)]
board = []
direction = []
for i in range(4):
    board.append([])
    direction.append([])
for i in range(4):
    for j in range(8):
        if j % 2 == 0:  # 4 x 4 좌표 값 추출
            board[i].append(data[i][j])
        else:  # direction 추출
            direction[i].append(data[i][j])

eat_fish = board[0][0]
pos_r, pos_c = 0, 0
shark_direction = direction[0][0]
