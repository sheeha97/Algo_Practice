"""
nm 포탑


각 포탑은 공격력 줄거나 늘어날수 있음
0 이하면 부서진다
최초에 0 가능

4가지 액션 수행
stop when 부서지지 않은 포탑 == 1


1. 공격자 선정
부서지지 않은 포탑 중 가장 약한 포탑 선정   
공격력 n + m 만큼 증가
약한 포탑 선정 기준
    1. 공격력이 가장 약한 거
    2. if 2개 이상 가장 최근에 공격한 포탑
    3. if same, 각 포탑 위치 행과 열이 가장 큰게 가장 약한 포탑
    4. if same 열 (row)이 가장 큰 포탑 (x 값)


2. 공격자의 공격
자신을 제외한 가장 강한 포탑을 공격
가장 강한 포탑 선정 기준
    1. 공격력이 가장 높은
    2. if 두개 공격한지 가장 오래된
    3. row + col 이 가장 작은
    4. row 값이 가장 작은

2.1    
try 레이져 공격 (우/하/좌/상) 우선순위
1. 상하좌우 4개의 방향으로 이동
2. 부서진 포탑 지나가기 x
3. 가장자리에서 막힌 방향으로 진행 할시 반대편으로 나옴 
    ex) (2,4) -> (2, 1)

최단 경로로 공격 if 안먹혀
포탄 공격 실시
피해 입으면 공격 당한 만큰 줄어듬
레이저 경로에 있는 애들도 데미지 half 만큼

2.2
포탄 공격
공격 대상에 포탄 던짐
공격력 만큰 피해
+ 8 방향 데미지 (절반만큼)
공격자는 데미지 안 받음
if 가장 자리 데미지 then 레이저 와 똑같이 데미지


3. 데미지 받은 포탑 철거

4. 포탑 정비
if not 공격자 or 공격받음 공격력 + 1

가장 강한 포탑 공격력 출력

4 4 4
0 1 4 4
8 0 10 13
8 0 11 26
0 0 0 0



4 4 1
0 1 4 4
8 0 10 13
8 0 11 26
0 0 0 0

-> 17



4 4 1
0 0 26 0
0 26 1 13
26 1 1 26
0 26 0 0


4 4 1
2 1 0 4
2 0 10 13
8 0 11 26
0 0 0 0

4 4 1
2 1 0 4
0 0 0 0
8 0 11 26
0 0 0 0

4 4 1
2 1 0 4
0 0 0 0
8 0 11 0
0 0 0 26

4 4 1
1 2 0 0
2 0 0 0
0 0 11 3
0 0 4 26


10 6 1000
3362 3908 4653 3746 4119 3669
4174 0 0 868 1062 854
633 51 759 0 4724 1474
2735 365 1750 3382 498 1672
141 3700 0 436 2752 974
3494 0 4719 2016 3870 0
3357 0 4652 3468 0 3758
4610 3125 0 2364 3303 1904
0 0 0 0 3959 3324
3187 0 105 2821 3642 160


-->727

"""
from collections import deque
n, m, k = map(int, input().split())
graph = []
tower_list = []
time_dict = {}
global_counter = 0
not_attacked = {}

dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]

for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range(m):
        value = graph[i][j]
        if value > 0:
            # value, x, y
            tower_list.append((value, i, j))
            time_dict[(i, j)] = 0
            not_attacked[(i, j)] = 1

"""
return tower (attack, x, y)
"""
def select_attacker():
    smallest_power_tower = (1e9, -1, -1)
    min_power = 1e9
    max_time = 0
    for tower in tower_list:
        power, x, y = tower
        time = time_dict[(x, y)]
        if power < min_power:
            smallest_power_tower = (power, x, y)
            min_power = power
            max_time = time
        elif power == min_power:
            # print("GOT IT")
            # print("INFO select attack: ", max_time, time, (x, y))
            if max_time < time:
                smallest_power_tower = (power, x, y)
                max_time = time
            elif max_time == time:
                if x + y == smallest_power_tower[1] + smallest_power_tower[2]:
                    if y > smallest_power_tower[2]:
                        smallest_power_tower = (power, x, y)
                elif x + y > smallest_power_tower[1] + smallest_power_tower[2]:
                    smallest_power_tower = (power, x, y)
        
    return smallest_power_tower

def search_strongest():
    strongest_power_tower = (0, 0, 0)
    max_power = 0
    min_time = 0
    for tower in tower_list:
        power, x, y = tower
        time = time_dict[(x, y)]
        if power > max_power:
            strongest_power_tower = (power, x, y)
            max_power = power
            min_time = time
        elif power == max_power:
            if min_time > time:
                strongest_power_tower = (power, x, y)
                min_time = time
            elif min_time == time:
                if x + y == strongest_power_tower[1] + strongest_power_tower[2]:
                    if y < strongest_power_tower[2]:
                        strongest_power_tower = (power, x, y)
                elif x + y < strongest_power_tower[1] + strongest_power_tower[2]:
                    strongest_power_tower = (power, x, y)
    return strongest_power_tower


def attack_tower(value, x, y):
    global graph
    global time_dict
    target_power, target_x, target_y = search_strongest()
    attack_power = value + n + m
    graph[x][y] = attack_power
    path = laser_attack(x, y, target_x, target_y)
    # print("THIS IS THE ATTACK INFO : ", (target_x, target_y, target_power), (x, y, value))
    # print(path)
    # do the 포탄 공격

    if path == []:
        # print("포탄 공격")
        for i in range(8):
            nx = target_x + dx[i]
            ny = target_y + dy[i]

            if nx < 0:
                nx = n - 1
            elif nx >= n:
                nx = 0

            if ny < 0:
                ny = m - 1
            elif ny >= m:
                ny = 0

            tower_power = graph[nx][ny]
            if (nx == x and ny == y) or tower_power == 0:
                continue
            tower_power -= (attack_power // 2)
            if tower_power <= 0:
                # print("INFO: ", (nx, ny), tower_power, graph[nx][ny])
                graph[nx][ny] = 0
                time_dict.pop((nx, ny))
                not_attacked.pop((nx, ny))
            else:
                graph[nx][ny] = tower_power
                not_attacked[(nx, ny)] = 0


    else:
        # print("레이져 공격")
        # attack on its way
        for tower in path:
            path_x, path_y = tower
            tower_power = graph[path_x][path_y]
            if path_x == x and path_y == y:
                continue
            tower_power -= (attack_power // 2)
            if tower_power <= 0:
                graph[path_x][path_y] = 0
                time_dict.pop((path_x, path_y))
                not_attacked.pop((path_x, path_y))
            else:
                graph[path_x][path_y] = tower_power
                not_attacked[(path_x, path_y)] = 0
        
    # damage the target
    damage = target_power - attack_power
    
    if damage <= 0:
        graph[target_x][target_y] = 0
        time_dict.pop((target_x, target_y))
        not_attacked.pop((target_x, target_y))
    else:
        graph[target_x][target_y] = damage
        not_attacked[(target_x, target_y)] = 0
    
    time_dict[(x, y)] = global_counter
    not_attacked[(x, y)] = 0
    # print("This is the result of the attack")
    # for i in range(n):
    #     print(graph[i])


def laser_attack(start_x, start_y, target_x, target_y):
    queue = deque([(start_x, start_y, [(start_x, start_y)])])
    visited = [[0 for _ in range(m)] for _ in range(n)]

    while queue:
        x, y, path = queue.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0:
                nx = n - 1
            elif nx >= n:
                nx = 0

            if ny < 0:
                ny = m - 1
            elif ny >= m:
                ny = 0

            if visited[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                continue
            elif nx == target_x and ny == target_y:
                return path

            queue.append((nx, ny, path + [(nx, ny)]))
    
    return []


def increase_attack():
    global graph
    global not_attacked
    for key in not_attacked.keys():
        if not_attacked[key] == 1:
            graph[key[0]][key[1]] += 1
            # print("Increase ", (key[0], key[1]))

    # reset
    not_attacked = {}
    for key in time_dict.keys():
        not_attacked[key] = 1


while global_counter < k:
    global_counter += 1
    # select attacker
    value, x, y = select_attacker()
    attack_tower(value, x, y)
    # print("THIS IS TIME DICT AFFTER ATTACT")
    # print(time_dict)
    increase_attack()
    # for i in range(n):
    #     print(graph[i])


    tower_list = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                tower_list.append((graph[i][j], i, j))
    
    if len(time_dict) == 1:
        break

print(search_strongest()[0])

