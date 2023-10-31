"""
n, k 어항정리 사이즈 와 가장 큰 거와 작은거의 차이를 k 될떄까지 필요한 정리 숫자를 return

1. 가장 적은 수의 어항들 물고기 add + 1
2. 맨 왼쪽을 올림
3. 들어서 올림



8 7
5 2 3 14 9 2 11 8

12 7
5 2 3 14 9 2 11 8 7 7 7 7

16 7
5 2 3 14 9 2 11 8 7 7 7 7 6 6 6 6

20 7
5 2 3 14 9 2 11 8 2 4 8 1000 7 7 7 9999 5 9999 5 5

28 7
5 2 3 14 9 2 11 8 7 7 7 7 6 6 6 6 5 2 3 14 9 2 11 8 7 7 7 7

4 5
1 2 3 4

12 3
2 100 100 1000 100 100 1000 100 100 100 100 50



28 0
2070 219 1956 1304 1321 1024 2793 1455 2596 816 17 1394 2669 1442 80 229 1763 516 960 2387 1461 2534 246 1064 1409 111 1642 465 


"""
# 1 = 상, 2 =  left , 3= 하 4 = right

n, k = map(int, input().split())

dx = [0, -1, 0, 1, 0]
dy = [0, 0, -1, 0, 1]


# dx_construct = [0, 1, 0, -1, 0]
# dy_construct = [0, 0, -1, 0, 1]

# -1 means there is nothing
cage_2d = [[-1 for _ in range(n)] for _ in range(n)]

cage_1d_2_2d = {}

fish_cage = list(map(int, input().split()))

max_num = 0
min_num = 1e9
diff = 0

for num in fish_cage:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
    
diff = max_num - min_num

def add_fish():
    global fish_cage
    min_list = []
    min_num = 1e9
    for i in range(len(fish_cage)):
        if min_num > fish_cage[i]:
            min_list = [i]
            min_num = fish_cage[i]
        elif min_num == fish_cage[i]:
            min_list.append(i)
    
    for idx in min_list:
        fish_cage[idx] += 1
"""
# 1 = 상, 2 =  left , 3= 하 4 = right
# 1 = 상, 2 =  left , 3= 하 4 = right

"""
def restructure(x, y):
    num_block_2_move = 2
    block_2_move_counter = 2

    left_over_block = n - num_block_2_move
    dir = 1

    idx_x_counter = 3
    idx_y_couunter = 1


    while num_block_2_move <= left_over_block:
        dir += 1
        if dir == 5:
            dir = 0
        
        block_2_move_counter -= 1
        left_over_block -= num_block_2_move

        if block_2_move_counter == 0:
            num_block_2_move += 1
            block_2_move_counter = 2

        idx_x_counter -= 1
        idx_y_couunter -= 1

        if idx_x_counter == 0:
            x += 1
            idx_x_counter = 4
        
        if idx_y_couunter == 0:
            y += 1
            idx_y_couunter = 4
    
    return x, y, dir, left_over_block

"""
1 = 상, 2 = right , 3= 하 4 = left
"""
def construct(x, y, dir, left_over_block):
    global cage_2d
    global cage_1d_2_2d
    cage_2d = [[-1 for _ in range(n)] for _ in range(n)]

    cage_1d_2_2d = {}
    dir_counter = 1
    dir_num = 1
    dir_num_counter = 2

    for i in range(n - left_over_block):
        print("This is the grid ", (x,y), " and the value ", (i, fish_cage[i]))
        cage_2d[x][y] = fish_cage[i]
        cage_1d_2_2d[i] = (x, y)

        if i == n - left_over_block - 1:
            break

        x = x + dx[dir]
        y = y + dy[dir]

        dir_counter -= 1
        if dir_counter == 0:
            dir_num_counter -= 1
            if dir_num_counter == 0:
                dir_num += 1
                dir_num_counter = 2

            dir -= 1
            if dir == 0:
                dir = 4
        
            dir_counter = dir_num


    for i in range(left_over_block):
        y += 1
        cage_2d[0][y] = fish_cage[n - left_over_block + i]
        cage_1d_2_2d[n - left_over_block + i] = (0, y)
        print("This is the grid for leftover ", (0, y))
    
def divide_fish():
    global cage_2d
    
    new_cage_2d = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_cage_2d[i][j] = cage_2d[i][j]

    for i in range(n):
        x, y = cage_1d_2_2d[i]
        if cage_2d[x][y] == -1:
            continue
        for dir in range(1, 5):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx and nx < n and 0 <= ny and ny < n and cage_2d[nx][ny] != -1:
                diff = abs(cage_2d[x][y] - cage_2d[nx][ny])
                val = diff // 5
                if val >= 1:
                    if cage_2d[x][y] > cage_2d[nx][ny]:
                        new_cage_2d[x][y] -= val
                    else:
                        new_cage_2d[x][y] += val

    for i in range(n):
        for j in range(n):
            cage_2d[i][j] = new_cage_2d[i][j]


def reconstruct():
    global fish_cage
    new_cage = [0 for _ in range(n)]
    x = 0
    y = 0
    added = 0
    while True:
        if added == n:
            # print("Break point 1")
            break
        if 0 <= x and x < n and 0 <= y and y < n:        
            if x > 0 and cage_2d[x][y] == -1:
                x = 0
                y += 1
            elif x == 0 and cage_2d[x][y] == -1:
                # print("Break point 2")
                break
            elif cage_2d[x][y] != -1:
                new_cage[added] = cage_2d[x][y]
                added += 1
                x += 1
            else:
                break
        else:
            # print("Breakk point 2")
            break
    
        
    max_val = 0
    min_val = 1e9

    for i in range(n):
        if new_cage[i] > max_val:
            max_val =  new_cage[i]
        if new_cage[i] < min_val:
             min_val =  new_cage[i]
        fish_cage[i] = new_cage[i]


    return max_val - min_val

def flip_twice():
    global cage_2d
    global cage_1d_2_2d

    cage_2d = [[-1 for _ in range(n)] for _ in range(n)]
    cage_1d_2_2d = {}
    length = n // 4
    start = 0
    x, y = (0, 0)
    for i in range(2):
        if i == 0:
            start = length * 3
            x, y = (0, 0)
        else:
            start = length * 1
            x, y = (2, 0)
        for j in range(length):
            cage_2d[x][y] = fish_cage[start + j]
            cage_1d_2_2d[start + j] = (x, y)
            y += 1

    for i in range(2):
        if i == 0:
            start = length * 0
            x, y = (1, 0)
        else:
            start = length * 2
            x, y = (3, 0)
        for j in range(length - 1, -1, -1):
            cage_2d[x][y] = fish_cage[start + j]
            cage_1d_2_2d[start + j] = (x, y)
            y += 1

counter = 0

while diff > k:
    counter += 1
    # 1. 
    add_fish()
    print("This is the fc ", fish_cage)
    # 2. 하나만 올린다
    first_x = 1
    first_y = 0

    #3 -1 . 반복적으로 쌓아 올리며 첫 번쨰의 좌표를 찾습니다
    x, y, dir, left_over_block = restructure(first_x, first_y)
    print("This is the INFO: ", x, y, dir, left_over_block)

    # 3-2 좌표를 바탕으로 2d로 만듭니다
    construct(x, y, dir, left_over_block)
    print("This is after the construction ")
    print(fish_cage)
    print("and the 2d cage")
    for i in range(n):
        print(cage_2d[i])
    
    print("---------------------------------------------")
    print("---------------------------------------------")
    print("---------------------------------------------")

    # 4 divide fish
    divide_fish()
    # print("After dividing the fish")
    # for i in range(n):
    #     print(cage_2d[i])

    # 5. reconstruct
    reconstruct()
    # print("After reconstruct fc", fish_cage)
    # print("The dictionary ", cage_1d_2_2d)

    # 6. flip_twice
    flip_twice()
    # print("After flipping twice")
    # for i in range(n):
    #     print(cage_2d[i])
    # print("The dictionary ", cage_1d_2_2d)

    print("---------------------------------------------")
    print("---------------------------------------------")
    print("---------------------------------------------")
    # 7 divide fish again
    divide_fish()
    # print("After dividing again ")
    # for i in range(n):
    #     print(cage_2d[i])

    diff = reconstruct()
    print("After THE WHOLE THING", fish_cage)
    print("THIS THE DIFF VALUE ", diff)

print(counter)


