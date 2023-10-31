"""
토끼들 경주
4:40
1.
p마리의 토끼 고유 번호 + 한번 이동시 이동해야하는 거리
전부 1, 1 에 있음 
n * m 격자

2. 경주 진행
우선순위가 높은 토끼를 뽀ㅃ아 멀리 보내주눈 것을 k번 반복
우선순위
    1. 현재까지 총 점프 횟수가 적은 토끼
    2. 행 + 열 번호가 작은 토끼
    3. 행이 작은 토끼
    4. 열이 작은 토끼
    5. 고유 번호가 작은 토끼

상하좌우 네방향으로 각각 di 만큰 이동 했을때 위치 구합니다
if 격자를 벗어나게 되면 --> 방향을 바꿔 반대로 한칸
    1. 행번호 + 열번호가 큰 칸
    2. 행번호가 큰칸
    3. 열 번호가 큰칸

    이 우선순위 대로 갈 칸을 선정
    이후 나버지 p-1 토끼 들은 전부 ri +ci 만큰의 점수를 동시에 얻음

k번 진행 후 
    1. 행 + 열번호가 큰 토끼
    2. 행 이 큰 토끼
    3. 열이 큰 토끼
    4. 고유 번호가 큰 토끼 순으로 우선 순위를 움
이 토끼 에게 S 점수를 더해 줍니다
****  k번의 턴 동안 한번이라도 뽑혔던 적이 있던 토끼 들 중에 우선순위

3. 이동거리 변경
고유번호가 pidt인 토끼의 이동 거리를 L배 해줍니다 (특정 토끼의 이동거리가 10억을 넘어가는 일 없음)

4. 각 토끼가 모든 경주를 진해ㅇ하며 얻은 점수 중 가장 높은 점수 출력
q번에 걸쳐 명령을 선정


5
100 3 5 2 10 2 20 5
200 6 100
300 10 2
200 3 20
400



"""
from collections import deque
q = int(input())
n = 0
m = 0
p = 0
k = 0
s = 0

rabbits = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


class Rabbit:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
        self.num_jump = 0
        self.x = 1
        self.y = 1
        self.point = 0

def select_rabbit():

    selected_rabbit = rabbits[0]

    for rabbit in rabbits:
        if rabbit.num_jump < selected_rabbit.num_jump:
            selected_rabbit = rabbit
        elif rabbit.num_jump == selected_rabbit.num_jump:
            if rabbit.x + rabbit.y < selected_rabbit.x + selected_rabbit.y:
                selected_rabbit = rabbit
            elif rabbit.x + rabbit.y == selected_rabbit.x + selected_rabbit.y:
                if rabbit.x < selected_rabbit.x:
                    selected_rabbit = rabbit
                elif rabbit.x == selected_rabbit.x:
                    if rabbit.y < selected_rabbit.y:
                        selected_rabbit = rabbit
                    elif rabbit.y == selected_rabbit.y:
                        if rabbit.id < selected_rabbit.id:
                            selected_rabbit = rabbit
    
    return selected_rabbit


def race():
    selected_rabbit = select_rabbit()
    distance = selected_rabbit.dist

    dest_x = -1
    dest_y = -1

    for i in range(4):
        dir = i
        counter = 0
        nx = selected_rabbit.x
        ny = selected_rabbit.y

        while counter < distance:
            counter += 1
            nx = nx + dx[dir]
            ny = ny + dy[dir]

            if nx == 0:
                nx += 2
                dir = 1
            elif nx > n:
                nx -= 2
                dir = 0

            elif ny == 0:
                ny += 2
                dir = 3
            elif  ny > m:
                ny -= 2
                dir = 2

        if nx + ny > dest_x + dest_y:
            dest_x = nx
            dest_y = ny
        elif nx + ny == dest_x + dest_y:
            if nx > dest_x:
                dest_x = nx
                dest_y = ny
            elif nx == dest_x:
                if ny > dest_y:
                    dest_x = nx
                    dest_y = ny

        

    # now move the rabbit and add up the points
    selected_rabbit.x = dest_x
    selected_rabbit.y = dest_y
    selected_rabbit.num_jump += 1
    for rabbit in rabbits:
        if rabbit.id != selected_rabbit.id:
            rabbit.point += (dest_x + dest_y)
            # print("Rabbit ", rabbit.id, " earned point ", rabbit.point)
    
    return selected_rabbit


def select_point_rabbit(jump_list):
    selected_rabbit = jump_list[0]

    for rabbit in jump_list:
        if rabbit.x + rabbit.y > selected_rabbit.x + selected_rabbit.y:
            selected_rabbit = rabbit
        elif rabbit.x + rabbit.y == selected_rabbit.x + selected_rabbit.y:
            if rabbit.x > selected_rabbit.x:
                selected_rabbit = rabbit
            elif rabbit.x == selected_rabbit.x:
                if rabbit.y > selected_rabbit.y:
                    selected_rabbit = rabbit
                elif rabbit.y == selected_rabbit.y:
                    if rabbit.id < selected_rabbit.id:
                        selected_rabbit = rabbit
        
    return selected_rabbit




for _ in range(q):
    line = list(map(int, input().split()))
    if line[0] == 400:
        max_point = 0
        for rabbit in rabbits:
            if rabbit.point > max_point:
                max_point = rabbit.point
        print(max_point)

    if line[0] == 100:
        n = line[1]
        m = line[2]
        p = line[3]
        for i in range(p):
            # (id, dist)
            rabbit = Rabbit(line[i * 2 + 4], line[i * 2 + 5])
            rabbits.append(rabbit)
        
        # print("This is rabbits")
        # for rabbit in rabbits:
        #     print(rabbit.id)

        # # test for select rabbit
        # print("This is selected rabbits")
        # rabbit = select_rabbit()
        # print(rabbit.id, rabbit.x, rabbit.dist)

    if line[0] == 200:
        k = line[1]
        s = line[2]
        jumped_list = []
        while k > 0:
            selected_rabbit = race()
            # print("Rabbit ", selected_rabbit.id, " jumped")
            # print("And the new location is ", (selected_rabbit.x, selected_rabbit.y))
            # print("And its distance is ", selected_rabbit.dist)

            jumped_list.append(selected_rabbit)
            k -=1
        point_rabbit = select_point_rabbit(jumped_list)
        point_rabbit.point += s        

        # print("Winner")
        # print(point_rabbit.point, point_rabbit.id, point_rabbit.x, point_rabbit.y)

    if line[0] == 300:
        p_id = line[1]
        l = line[2]
        for rabbit in rabbits:
            if rabbit.id == p_id:
                # print("BEFORE ", rabbit.dist)
                rabbit.dist *= l
                # print("Changed distance of rabbit ", rabbit.id, " to ", rabbit.dist)
                break

    # print(rabbits, k, s)