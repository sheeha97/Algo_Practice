"""

move
rain
copy
find_next


1  2    3   4    5    6    7    8 
서 북서 북  북동  동   남동 남    남서
"""


n, m = map(int, input().split())
graph = []
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

dir_length_list = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

for _ in range(m):
    d, ss = map(int, input().split())
    dir_length_list.append((d, ss))


"""
helper
"""
def check(x):
    if 0 <= x and x < n:
        return True
    return False

"""
move the cloud
and add the water in the bucket
"""
def move(x, y, d, s):
    # for s number of time move the cloud
    # print("Inital move is ", (x, y), " where the d and s is ", (d, s))
    nx = x
    ny = y
    for i in range(s):
        # the direction
        nx = nx + dx[d]
        ny = ny + dy[d]

        # check if its within the range
        if check(nx) and check(ny):
            continue
        else:
            if not check(nx):
                # case for nx going to the bottom
                if nx < 0:
                    nx = n -1
                elif nx >= n:
                    nx = 0
            if not check(ny):
                if ny < 0:
                    ny = n -1
                elif ny >= n:
                    ny = 0
    
    # now the move is finished, we want to add the bucket
    # print("Now adding the grid for ", (nx, ny))
    graph[nx][ny] += 1

    return (nx, ny)


"""
copy water
"""
def copy_water(x, y):
    #check the crosses
    for d in [2, 4, 6, 8]:
        nx = x + dx[d]
        ny = y  + dy[d]

        # 거리가 1인 대각선 칸
        if check(nx) and check(ny):
            if graph[nx][ny] >= 1:
                graph[x][y] += 1

    return

def create_cloud(cloud_dict):
    ret_list = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2 and cloud_dict.get((i, j)) is None:
                ret_list.append((i, j))
                graph[i][j] -= 2

    return ret_list

# after m movement
total = 0
move_list = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
temp_list = []

for d, s in dir_length_list:
    cloud_dict = {}
    temp_list = []
    for x, y in move_list:
        nx, ny = move(x, y, d, s)
        temp_list.append((nx, ny))

        # add to cloud dict
        cloud_dict[(nx, ny)] = 0
        
    # print("After move")
    # for i in range(n):
    #     print(graph[i])

    # print("This is the next temp list ", move_list)

    # now that we finished moving, add the 
    for x, y in temp_list:
        copy_water(x, y)


    # print("After copy water")
    # for i in range(n):
    #     print(graph[i])

    # print("")

    # now create cloud
    move_list = create_cloud(cloud_dict)
    # print("After create cloud")
    # for i in range(n):
    #     print(graph[i])

    # print("This is the next move list ", move_list)

# print("This is a test: ")
# for i in range(n):
#     print(graph[i])

for i in range(n):
    for j in range(n):
        if graph[i][j] > 0:
            total += graph[i][j]

print(total)