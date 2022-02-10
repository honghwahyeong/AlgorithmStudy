from copy import deepcopy

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dice_direction = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]  # 0왼 1오 2앞 3위 4뒤 5아래

for direction in dice_direction:
    tmp_dice = deepcopy(dice)
    nx = x + dx[direction]
    ny = y + dy[direction]
    if 0 <= nx < n and 0 <= ny < m:
        if direction == 1:  # 동
            dice[0] = tmp_dice[5]
            dice[5] = tmp_dice[1]
            dice[3] = tmp_dice[0]
            dice[1] = tmp_dice[3]
        elif direction == 2:  # 서
            dice[1] = tmp_dice[5]
            dice[0] = tmp_dice[3]
            dice[5] = tmp_dice[0]
            dice[3] = tmp_dice[1]
        elif direction == 3:  # 북
            dice[5] = tmp_dice[2]
            dice[4] = tmp_dice[5]
            dice[3] = tmp_dice[4]
            dice[2] = tmp_dice[3]
        elif direction == 4:  # 남
            dice[5] = tmp_dice[4]
            dice[4] = tmp_dice[3]
            dice[3] = tmp_dice[2]
            dice[2] = tmp_dice[5]

        if board[nx][ny] == 0:
            board[nx][ny] = dice[5]
        else:
            dice[5] = board[nx][ny]
            board[nx][ny] = 0

        print(dice[3])
        x, y = nx, ny
