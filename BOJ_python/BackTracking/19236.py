import sys
from copy import deepcopy

input = sys.stdin.readline
# 북 북서 서  남서 남  남동 동  북동
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def dfs(x, y, d, cnt):
    global answer, data, fish
    move(x, y)
    while True:
        nx = x+dx[d]
        ny = y+dy[d]
        if not 0 <= nx < 4 or not 0 <= ny < 4:
            answer = max(answer, cnt)
            return
        if not data[nx][ny]:
            x, y = nx, ny
            continue
        # data,fish,상어가 먹게 될 물고기 정보 tmp 저장
        tmp_data, tmp_fish = deepcopy(data), deepcopy(fish)
        tmp1, tmp2 = fish[data[nx][ny][0]], data[nx][ny]
        fish[data[nx][ny][0]], data[nx][ny] = [], []
        # 상어 다음 좌표, 먹은 물고기의 방향, 지금까지 먹은 크기 + 먹은 물고기 크기+1 재귀
        dfs(nx, ny, tmp2[1], cnt+tmp2[0]+1)
        # 변수들 다시 리셋
        data, fish = tmp_data, tmp_fish
        fish[data[nx][ny][0]], data[nx][ny] = tmp1, tmp2
        x, y = nx, ny


def move(sx, sy):
    for i in range(16):
        if fish[i]:
            x, y = fish[i][0], fish[i][1]
            for _ in range(9):
                nx = x + dx[data[x][y][1]]
                ny = y + dy[data[x][y][1]]
                if not 0 <= nx < 4 or not 0 <= ny < 4 or (nx == sx and ny == sy):
                    data[x][y][1] = (data[x][y][1]+1) % 8  # 방향 회전
                    continue
                if data[nx][ny]:
                    fish[data[nx][ny][0]] = [x, y]
                data[nx][ny], data[x][y] = data[x][y], data[nx][ny]
                fish[i] = [nx, ny]
                break


data = [[] for _ in range(4)]
fish = [[] for _ in range(16)]

for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(0, 7, 2):
        data[i].append([tmp[j]-1, tmp[j+1]-1])
        fish[tmp[j]-1] = [i, j//2]
answer = 0
d, cnt = data[0][0][1], data[0][0][0]+1
fish[data[0][0][0]], data[0][0] = [], []
dfs(0, 0, d, cnt)
print(answer)
