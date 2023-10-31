"""

1 - m 상어 unique
1이 가장 강력하다 (영역 싸움)

n * n size board

1. 맨 처음 자기 칸 에다가 냄 새 뿌림
2. 모든 상어가 인접한 칸으로 이동
3. 냄새 뿌림 (방향도 바꿔야함)

--- if 한칸에 여려명의 상어 -> 젤 쎈애 빼고 다 방출

** 냄새 유지는 k초

이동 할때 조건
1. 먼저 냄새가 없는 칸으로 ㄱㄱ
2. 없으면 자신의 냄새 칸 ㄱㄱ

3. 만약 가능한 칸이 > 1
    - 우선순위 에 따라 다름 (every shark has there own 우선 순위)

상어 init 방향 주어짐
상어 방향은 이동 후 바뀜


ret 1번 상어만 격자에 남게 되기 까지 걸리는 시간

"""
from collections import deque


n, m, k = map(int, input().split())

# 위 아래 왼 오른
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

graph = []
# sharks : (x, y, dir)
sharks = [[0, 0, 0] for _ in range(m + 1)]
shark_dir_priority = {}
shark_num = m

# smell_graph = [[(0,0) for _ in range(n)] for _ in range(n)]
smells = {}



# print(sharks)

for i in range(n):
    line = list(map(int, input().split()))
    num_list = []
    for num in line:
        num_list.append([num])
    graph.append(num_list)
    for j in range(n):
        if line[j] > 0:
            sharks[line[j]] = [i, j, 0]

# print(sharks)

init_dir = list(map(int, input().split()))
for shark_num in range(1, m + 1):
    # print(sharks[shark_num])
    sharks[shark_num][2] = init_dir[shark_num - 1]

for shark_num in range(1, m + 1):
    shark_dir_priority[shark_num] = {}
    for i in range(1, 5):
        dir_list = list(map(int, input().split()))
        # print(dir_list)
        shark_dir_priority[shark_num][i] = dir_list

# print(graph)
# print(sharks)
# print(shark_dir_priority)


"""
check within graph
"""
def check(x, y):
    if 0 <= x and x < n and 0 <= y and y < n:
        return True
    return False


"""
bfs to run every move
"""
def bfs(shark_num):
    # print("Start BFS and m is ", m)
    # 우선 각 상어들은 자기 자리에 다가 냄새를 남깁니다
    for i in range(1, m + 1):
        shark_x = sharks[i][0]

        if shark_x == -1:
            # print("Deleted Shark info: ", i ," is ", shark_x)
            continue
        shark_y = sharks[i][1]
        # 그 상어 냄새로다가 set it
        # smell_graph[shark_x][shark_y] = (i, k)
        smells[(shark_x, shark_y)] = [i, k]


    for i in range(m, 0, -1):
        # print("This is ", i)
        shark_x = sharks[i][0]

        if shark_x == -1:
            # print("Deleted Shark info: ", i ," is ", shark_x)
            continue

        shark_y = sharks[i][1]
        shark_dir = sharks[i][2]
        next_dir_priority = shark_dir_priority[i][shark_dir]

        # 움직이기 전에 갈 수 있는 칸을 보고 우선 순위 정하기
        move_list = []
        eat = True
        for d in range(1, 5):
            nx = shark_x + dx[d]
            ny = shark_y + dy[d]

            # print("The new grid for ", i ," is ", (nx, ny))

            # 빈칸
            if check(nx, ny):
                if smells.get((nx, ny)) is None:
                    move_list.append(d)
        
        # 만약에 빈칸이 없으면 자기 영역으로 갑니다.
        if len(move_list) == 0:
            eat = False
            for d in range(1, 5):
                nx = shark_x + dx[d]
                ny = shark_y + dy[d]

                if check(nx, ny):
                    if smells.get((nx, ny)) is not None and smells[(nx, ny)][0] == i:
                        # print("shark ", i, "its time to go back ")
                        move_list.append(d)
        
        # 이제 여기서 우선순위에 따른 방향 결정 하기
        # 3412
        next_dir = 0
        if len(move_list) > 1:
            for move in next_dir_priority:
                if move in move_list:
                    next_dir = move
                    break
        elif len(move_list) == 1:
            next_dir = move_list[0]
        else:
            # print("SHARK CANT NOT MOVE ", i, " where the grid is ", (shark_x, shark_y))
            continue
        
        # 이제 움직입니다
        nx = shark_x + dx[next_dir]
        ny = shark_y + dy[next_dir]

        # 빈칸일때
        if graph[nx][ny][0] == 0:
            graph[nx][ny] = [i]
            # print("Shark ", i, " moved to empty ", (nx, ny), " from ", (shark_x, shark_y))

        # 다른 상어가 있을 때 상어 삭제 실시
        else:
            shark_to_delete = graph[nx][ny][0]
            if shark_to_delete < i:
                continue
            elif eat:
                sharks[shark_to_delete][0] = -1
                shark_num -= 1
                graph[nx][ny] = [i]
                # print("Shark ", i, " kicked ", shark_to_delete, "and went to ", (nx, ny), " from ", (shark_x, shark_y))

        # 상어가 지난 자리는 비워 둡니다 그리고 update
        sharks[i][0] = nx
        sharks[i][1] = ny
        sharks[i][2] = next_dir
        graph[shark_x][shark_y] = [0]
        # print("The shark is ", i ," and its next movement is ", (shark_x, shark_y), " to ", (nx, ny))

    # 이제 냄새를 처리 들어갑니다.
    remove_list = []
    for key in smells:
        smells[key][1] -= 1
        if smells[key][1] == 0:
            remove_list.append(key)
    
    for key in remove_list:
        # print("Remove smell that exists in ", key, " and the value is ", smells[key])
        smells.pop(key)

    # print("This is the updated graph")
    # for i in range(n):
    #     print(graph[i])

    # print("This is the updated smell_graph")
    # temp = [[(0, 0) for _ in range(n)] for _ in range(n)]
    # for key in smells:
    #     temp[key[0]][key[1]] = smells[key]
    #     # print("The smell information at ", key , " is ", smells[key])
    # for i in range(n):
    #     print(temp[i])

    return shark_num


time = 0
# test = 7
while True:
    # print("Leftover sharks", shark_num)
    if shark_num == 1:
        break
    elif time >= 1000:
        time = -1
        break
    shark_num = bfs(shark_num)
    time += 1

    # test
    # test -= 1

print(time)