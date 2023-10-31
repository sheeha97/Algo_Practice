"""

di, si = blizzard direction and length
1  2  3  4
상 하 좌 우



7 1
0 0 0 0 0 0 0
3 2 1 3 2 3 0
2 1 2 1 2 1 0
2 1 1 0 2 1 1
3 3 2 3 2 1 2
3 3 3 1 3 3 2
2 3 2 2 3 2 3
2 2

"""
from collections import deque


dx = [0, -1, 1, 0 ,0]
dy = [0, 0, 0, -1, 1]
graph = []
dir_list = []
marvel_list = []
#grid_list = []
marvel_2_grid = {}


n, m = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().split())))

for _ in range(m):
    di, si = map(int, input().split())
    dir_list.append((di, si))


def turn(dir):
    if dir == 3:
        return 2
    elif dir == 2:
        return 4
    elif dir == 4:
        return 1
    else:
        return 3

move_amount = 1
move_counter = move_amount
move_direction = 3
length_count = 1

shark_x = n//2
shark_y = n // 2

x = shark_x
y = shark_y
marvel_idx = 0
for i in range(n * n - 1):
    if length_count == 0:
        length_count = 2
        move_amount += 1
    
    if move_counter == 0:
        move_counter = move_amount
        move_direction = turn(move_direction)
        length_count -= 1
    

    # print("The previous grid is ", (x,y), " and the direction is ", move_direction)
    x = x + dx[move_direction]
    y = y + dy[move_direction]
    move_counter -= 1

    # print("Now the grid is ", (x,y))
    marvel_list.append(graph[x][y])
    # grid_list.append((x,y))
    marvel_2_grid[(x, y)] = marvel_idx
    marvel_idx += 1

"""
Destroy the marvels on its path and move

"""
def magic(d, s):
    x = shark_x
    y = shark_y
    while s > 0:
        x = x + dx[d]
        y = y + dy[d]
        marvel_idx = marvel_2_grid[(x, y)]
        marvel_list[marvel_idx] = -1
        # marvel_list.pop(marvel_idx + counter)
        # marvel_list.append(0)
        s -= 1

"""
arrange
"""
def arrange():
    global marvel_list
    del_count = marvel_list.count(-1)
    marvel_list = [marvel_list[i] for i in range(n * n - 1) if marvel_list[i] != -1]
    for _ in range(del_count):
        marvel_list.append(0)
    
    # print("This is marvel list in arrage:  ", marvel_list)
       


def explode():
    start_idx = 0
    point = 0
    while True:
        # print("This is marvel list in explode:  ", marvel_list)
        explode_list = []
        target = 0
        explode_counter = 1
        start_idx = 0
        for i in range(1, n * n - 1):

            if marvel_list[i] == marvel_list[target]:
                explode_counter += 1
            else:
                if explode_counter >= 4:
                    explode_list.append((start_idx, i))

                    # print("This is the details : ", start_idx, i)

                target = i
                explode_counter = 1
                start_idx = i
        
        if len(explode_list) == 0:
            break
        else:
            for start, end in explode_list:
                num = end - start
                for i in range(num):
                    point +=  marvel_list[start + i]
                    # print("add up the point", marvel_list[start + i])
                    marvel_list[start + i] = -1
                    # point += marvel_list.pop(start + counter)
                    # marvel_list.append(0)
            # print("This is marvel list after explode before arange :  ", marvel_list)
            arrange()

            
    return point


def re_build():
    if marvel_list[0] == 0:
        return

    start_idx = 0
    same_val = marvel_list[0]
    new_marvel_list = []
    size = n * n - 1

    for i in range(n * n - 1):
        if size <= 0:
            break

        if same_val != marvel_list[i]:
            new_marvel_list.append(i - start_idx)
            new_marvel_list.append(marvel_list[start_idx])

            size -= 2
            start_idx = i
            same_val = marvel_list[i]

        if marvel_list[i] == 0:
            break

    size = len(new_marvel_list)
    for i in range(n * n - 1):
        if i >= size:
            marvel_list[i] = 0
        else:
            marvel_list[i]= new_marvel_list[i]

# repeat this
total = 0
for d, s in dir_list:
    magic(d, s)
    # print("This is marvel list after magic :  ", marvel_list)
    arrange()
    # print("This is marvel list after arrange :  ", marvel_list)

    total += explode()
    re_build()

    # print("This is marvel list after rebuild :  ", marvel_list)

print(total)
