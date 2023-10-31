"""
03:45 ~ 04:07 -> 22분

04:25 ~

4 * 4 공간
각 칸 물고기 존재
물고기는 번호와 방향 존재

1. 1 <= 번호 <= 16 (same 번호는 exist x)
2. 방향은 8가지 (상하좌우 대각선)

** 처음에
1. 상어가 (0, 0) 물고기 먹고 방향은 그 물고기와 같다
2. 이후 물고기 이동 (move)
    - 물고기는 낮은 번호 순부터 이동
    - 한칸 이동 가능 
    - 이동 가능 한 칸: 빈 칸 or 다른 물고기가 있는 칸
    - 이동 못하는 칸: 상어 칸 or 공간 밖
    - 각 물고기는 방향이 이동 할수 있는 칸을 갈때까지 방향을 45도 반시계 회전 시킨다 (turn)
    - if 이동 할수 있는 칸 x 이동 x
    - 아닌 경우 그 칸으로 이동 
    - if 물고기가 다른 물고기 칸으로 이동 할때는 서로의 위치 변경 방식

3. 물고기 이동 끝나면 상어 이동
    - 방향에 있는 칸으로 이동 
    - 한번에 여러 개 칸 이동 가능
    - if 물고기 칸
        - 물고기 먹고 물고기 방향 얻음

    - ** 이동 하는 중 ** 에 있는 물고기 들은 안 먹음
    - 물고기가 없는 칸으로 이동 x
        - 그리고 칸 이 없으면 공간 벗어나 집으로 이동

4. repeat 2-3

graph:
0 -> 빈칸
1 ~ 16 : fish
-1 : shark

direction input:
1   2    3   4    5    6    7    8
북  북서 서  남서  남   남동  동   북동

ret: 상어가 먹을수 있는 물고기 번호 최댓값


"""

graph = []
test = []
fish_dict = {}
shark_dir = 0
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    line = list(map(int, input().split()))
    # 0 2 4 6
    num_dir_list = []
    test_list = []
    for k in range(4):
        value = line[k * 2]
        num_dir_list.append((value, line[k * 2 + 1]))
        test_list.append(value)
        if 1 <= value and value <= 16:
            fish_dict[value] = (i, k)

    test.append(test_list)
    graph.append(num_dir_list)


def check(x, y):
    if 0 <= x and x < 4 and 0 <= y and y < 4:
        return True
    return False


def turn(x, y, graph):
    counter = 8
    dir = graph[x][y][1]
    while counter >= 0:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if check(nx, ny) and graph[nx][ny][0] != -1:
            return dir
        counter -= 1
        dir += 1
        if dir > 8:
            dir = 1
    # nowhere to go

    
    return -1


def dfs(x, y, graph, fish_dict, score):
    global total_point

    # 상어가 먹는걸로 시작됩니다.
    fish_value = graph[x][y][0]
    shark_dir = graph[x][y][1]

    score += fish_value
    total_point = max(total_point, score)

    fish_dict.pop(fish_value)

    # 먹은 이 자리를 상어로 대체합니다.
    graph[x][y] = (-1, shark_dir)

    # 이제 물고기가 움직입니다.
    for i in range(1, 17):
        # 물고기가 아직 존재합니다
        if fish_dict.get(i) is not None:
            fish_x, fish_y = fish_dict[i]
            fish_dir = turn(fish_x, fish_y, graph)

            # 갈 곳을 잃은 불쌍한 물고기
            if fish_dir == -1:
                continue
            nx = fish_x + dx[fish_dir]
            ny = fish_y + dy[fish_dir]
            prev = graph[fish_x][fish_y]
            cur = graph[nx][ny]

            # 빈칸이든 물고기가 있든 바꿔줍니다.
            graph[nx][ny] = (prev[0], fish_dir)
            graph[fish_x][fish_y] = cur

            # fish dict 도 없데이트 해줍니다
            fish_dict[prev[0]] = (nx, ny)
            if fish_dict.get(cur[0]) is not None:
                fish_dict[cur[0]] = (fish_x, fish_y)

    # 이제 상어가 다음으로 먹을 물고기들을 찾고 재귀 합니다 (여기서 상어의 자리는 빈칸으로 만들어야 합니다.)
    if len(fish_dict) == 0:
        return total_point
    
    # 상어 방향으로 먹을 수 있는 모든 물고기 수집
    fish_list = []
    nx = x + dx[shark_dir]
    ny = y + dy[shark_dir]

    while check(nx, ny):
        if 1 <= graph[nx][ny][0] and graph[nx][ny][0] <= 16:
            fish_list.append(graph[nx][ny][0])
        nx += dx[shark_dir]
        ny += dy[shark_dir]
    
    if len(fish_list) == 0:
        return total_point
    
    for fish_val in fish_list:
        fish_x, fish_y = fish_dict[fish_val]
        temp = []
        for i in range(4):
            line = []
            for j in range(4):
                line.append(graph[i][j])
            temp.append(line)
        temp_dict = {}
        for key in fish_dict:
            temp_dict[key] = fish_dict[key]
        
        temp[x][y] = (0, 0)
        dfs(fish_x, fish_y, temp, temp_dict, score)
     

total_point = 0

dfs(0, 0, graph, fish_dict, 0)
print(total_point)
