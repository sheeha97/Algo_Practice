"""
n * n map, m fishes, 1 아기상어

아기 상어 크기 == 2, 1초에 상하좌우 이동 가능
1. if 자기 보다 큰 물고기 or 똑같은 물고기 x move
2. if 자기 보다 작은 물고기 먹을  수 있음 이동 ㄱ

아기 상어 이동 결정 방법
1. if 먹을수 있는 물고기 존재 x --> 엄마 상어 도움 요청
2. 먹을 수 있는 물고기 == 1 -> 먹으러 감
3. if 여러마리 먹을수 있어 --> 가장 가까운 물고기
    - 우선 순위로 가장 위, 가장 왼쪽

아기 상어 성장 방법
1. 자신의 크기와 같은 숫자의 물고기를 먹으면 increase
    - ex) size == 2 --> eat 2 --> size == 3

공간 주어졌을때 엄마 상어 도움 요청 없이 몇초 동안 

0 -> 빈 칸
1 ~ 6 물고기 크기 및 칸
9 -> 아기 상어 위치

ex) 
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4

"""
from collections import deque

# 다시

dx = [1, 0, -1, 0]
dy =[0, 1, 0, -1]
graph = []
time = 0
shark_x = 0
shark_y = 0
shark_size = 2
shark_counter = shark_size
n = int(input())
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 9:
            shark_x = i
            shark_y = j


"""
helper function to check if its within the board
"""
def check_board(x, y):
    if 0 <= x and x < n and 0 <= y and y < n:
        return True
    return False


"""
return the list of fishes that the shark can eat
"""
def bfs(start_x, start_y, shark_size):
    queue = deque([(start_x, start_y, 1)])
    visited = [[0 for _ in range(n)] for _ in range(n)]
    ret = []
    min_dist = 1e9
    while queue:
        x, y, dist = queue.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # check if its within the board + visited
            if check_board(nx, ny) and visited[nx][ny] == 0:
                # print("This is the beginning and nx ny is ", (nx, ny))
                board_value = graph[nx][ny]
                
                visited[nx][ny] = 1
                # fish is the same size or empty 칸
                if shark_size == board_value or board_value == 0:
                    # simply add the distance and append to queue
                    if dist <= min_dist:
                        queue.append((nx, ny, dist+1))
                        # print("This is what I appended !! ", (nx, ny), "and the value for visited ", visited[nx][ny])
            
                # if the shark is smaller do nothing
                elif shark_size < board_value:
                    continue
                # if the shark is bigger, append it to the eat list
                else:
                    if dist <= min_dist:
                        ret.append((nx, ny, dist))
                        min_dist = dist
                        # print(nx, ny, dist, min_dist)
                        # print(ret)

    ret.sort(key=lambda a: (a[0], a[1]))       
    return ret

time = 0
dist = 0
while True:
    fish_list = bfs(shark_x, shark_y, shark_size)
    if len(fish_list) == 0:
        break
    
    fish_x, fish_y, dist = fish_list[0]
    # print("INFO for eating ", (fish_x, fish_y, dist))
    graph[fish_x][fish_y] = 9
    graph[shark_x][shark_y] = 0
    
    # do the things for the shark
    shark_x = fish_x
    shark_y = fish_y
    shark_counter -= 1

    if shark_counter == 0:
        shark_size += 1
        shark_counter = shark_size

    time += dist

print(time)