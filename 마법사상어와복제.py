"""
4 * 4 격자

m마리의 물고기, 각물고기는 격자 한칸 + 이동방향 (상하좌우 대각선), 상어도 격자 한칸
(둘 이상의 물고기 한 격자 okay, 상어와 물고기 okay)

1. 마법사 상어가 모든 물고기에게 복제, 5번에서 물고기가 복제되어 나타나ㅡㅁ
2. 모든 물고기가 한칸 이동, 상어가 있는칸, 물고기의 냄새가 있는칸, 격자 외 칸 이동 x, 이동 못하면 가능 할때까지 45도 반시계 회전, 없으면 이동 x
3. 상어가 연속해서 3칸 이동, 상어는 상하좌우 이동 가능, if 연속해서 이동 할때 격자 벗어나면 불가능한 방법, 만약 물고기 있는 칸 지나면 그 칸에 있 는 물고기는 전부 제외, 그리고 냄새를 남김, 
    - 가능한 방법 중, 제외가 가장 많이 가능한 칸으로 감, if 여러가지, 사전 방법 참고
4. 두번 전 연습에서 생긴 물고기의 냄새가 사라진다
5. 복제된 모든 물고기 생성, 1의 위치와 방향을 가짐

상: 1 좌: 2 하: 3 우: 4
사전적
 132 < 343, so perform 132


 서: 1, 북서: 2, 북: 3, 북동: 4, 동: 5, 남동: 6, 남: 7, 남서: 8

 

6 1
4 3 5
1 3 5
2 4 2
2 1 6
3 4 4
3 4 3
4 2

"""
from collections import deque


m, s = map(int, input().split())

fish_map = {}
smell_map = {}

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
shark_dx = [0, -1, 0, 1, 0]
shark_dy = [0, 0, -1, 0, 1]
total_fish = m


for _ in range(m):
    x, y, val = map(int, input().split())
    if fish_map.get((x, y)) is None:
        fish_map[(x, y)] = [val]
    else:
        fish_map[(x, y)].append(val)


shark_x, shark_y = map(int, input().split())


def copy_fish():
    global fish_map
    temp_fish = {}
    for key in fish_map.keys():
        temp_fish[key] = fish_map[key]

    return temp_fish


def turn(x, y, dir):
    
    counter = 0
    while counter < 8:
        nx = x + dx[dir]
        ny = y + dy[dir]

        # print("The value for nx and ny is", (nx, ny), " where prev it was ", (x,y), " also test ", smell_map.get((nx, ny)))
        # print("This is shark ", shark_x, shark_y)
        if 0 < nx and nx <= 4 and 0 < ny and ny <= 4:
            if nx != shark_x or ny != shark_y:
                if smell_map.get((nx, ny)) is None:
                    return (nx, ny, dir)
        
        dir -= 1
        if dir == 0:
            dir = 8

        counter += 1

    return (x, y, dir)


def move():
    global fish_map
    new_map = {}
    for key in fish_map.keys():
        x, y = key
        fish_dir_list = fish_map[key]
        for dir in fish_dir_list:
            nx, ny, n_dir = turn(x, y, dir)
            # print("New value ", (nx, ny, n_dir), " before it was ", (x, y, dir), "also this is test, ", new_map.get((nx, ny)))
            if new_map.get((nx, ny)) is None:
                new_map[(nx, ny)] = [n_dir]
            else:
                new_map[(nx, ny)].append(n_dir)
    # print("This is new ", new_map)
    fish_map = new_map


def check(x, y):
    if 0 < x and x <= 4 and 0 < y and y <= 4:
        return True
    return False

        
"""
bfs 사전적
"""
def move_shark():
    global shark_x
    global shark_y
    global fish_map
    global total_fish
    # x, y, eat_num, move
    # visited = [[0 for _ in range(4)] for _ in range(4)]
    queue = deque([(shark_x, shark_y, 0, [], "")])
    max_food = 0
    max_moves = "999"
    max_grids = []
    while queue:
        x, y, eat_num, grids, moves = queue.popleft()
        # visited[x-1][y-1] = 1
        if len(grids) == 3:
            if max_food < eat_num:
                max_food = eat_num
                max_moves = moves
                max_grids = grids
            # case for equal number of fish
            elif max_food == eat_num:
                # print("INFO: ", x, y, moves, max_moves)
                if int(max_moves) > int(moves):
                    # print("Before ", max_moves, max_grids)
                    max_moves = moves
                    max_grids = grids
                    # print("Selected ", max_moves, max_grids)
        else:
            for i in range(1, 5):
                nx = x + shark_dx[i]
                ny = y + shark_dy[i]
                if not check(nx, ny):
                    continue
                # if visited[nx - 1][ny - 1] == 1:
                #     continue
                # 물고기가 있는 경우
                if fish_map.get((nx, ny)) is not None and not (nx, ny, 1) in grids:
                    fish_list = fish_map[(nx, ny)]
                    queue.append((nx, ny, eat_num + len(fish_list), grids + [(nx, ny, 1)], moves + str(i)))
                else:
                    queue.append((nx, ny, eat_num, grids + [(nx, ny, 0)], moves + str(i)))

    shark_x = max_grids[2][0]
    shark_y = max_grids[2][1]
    # print("These are the values ", (max_food, max_moves, max_grids), " and the changed shark xy ", (shark_x, shark_y))
        
    # max_food, max_moves, max_grids
    state = 0
    for grid in max_grids:
        x, y, state = grid
        if fish_map.get((x, y)) is not None and state == 1:
            fish_map.pop((x, y))
        if state == 1:
            smell_map[(x, y)] = 2

    total_fish -= max_food
    # print("This is the total fish change ", total_fish, " and ", max_food)


def remove_smell():
    global smell_map
    keys = smell_map.keys()
    remove_list = []
    for key in keys:
        smell_map[key] -= 1
        if smell_map[key] < 0:
            remove_list.append(key)
    for key in remove_list:
        smell_map.pop(key)


for _ in range(s):
    # 1. copy the current fish_map
    temp_fish = copy_fish()
    # print("This is copied temp fish")
    # print(temp_fish)
    # 2.
    move()
    # print(fish_map)
    # print("AFTER THE MOVE ONLY")
    # print(fish_map)
    # print(smell_map)
    # print(total_fish)

    # 3. 
    move_shark()

    # 4. remove smell
    remove_smell()

    # This is before the copy paste
    # print("This is before the copy paste")
    # print(fish_map)

    # 5. add copied fish
    for key in temp_fish.keys():
        total_fish += len(temp_fish[key])
        if fish_map.get(key) is not None:
            fish_map[key].extend(temp_fish[key])
        else:
            fish_map[key] = temp_fish[key]

    # print("AFTER THE WHOLE PROCESS")
    # print(fish_map)
    # print(smell_map)
print(total_fish)
    # print(shark_x, shark_y)
    




