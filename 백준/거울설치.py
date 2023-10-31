from collections import deque

"""
5
***#*
*.!.*
*!.!*
*.!.*
*#*** 

2

"""
n = int(input())

graph = []

doors = []
visited = [[[-1 for _ in range(4)] for _ in range(n)] for _ in range(n)]
    
for i in range(n):
    line = list(input())
    # print(line)
    graph.append(line)
    for j in range(n):
        if graph[i][j] == "#":
            doors.append((i, j))

# print(graph)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

start_x, start_y = doors[0]
end_x, end_y = doors[1]


start = []
for i in range(4):
    nx = start_x + dx[i]
    ny = start_y + dy[i]

    if 0 <= nx and nx < n and 0 <= ny and ny < n:
        if graph[nx][ny] != "*":
            start.append((start_x, start_y, i, 0))

queue = deque(start)

# print("Details : ", (start_x, start_y, end_x, end_y))
# print(queue)

ret = float('inf')
# ret = []

while queue:
    x, y, dir, num_mirror = queue.popleft()
    visited[x][y][dir] = num_mirror
    nx = x + dx[dir]
    ny = y + dy[dir]
    # print("First for nx and ny ", (nx, ny, dir, x, y))
    # print("Time for nx and ny ", (nx, ny, dir, num_mirror))

    if 0 <= nx and nx < n and 0 <= ny and ny < n:

        if visited[nx][ny][dir] == -1 or visited[nx][ny][dir] > visited[x][y][dir]:
            
            # print("Check for nx and ny ", (nx, ny, dir, graph[nx][ny], num_mirror))
            if nx == end_x and ny == end_y:
                ret = min(ret, visited[x][y][dir])
                # ret.append(num_mirror)
                # break

            if graph[nx][ny] == "*":
                continue
            elif graph[nx][ny] == ".":
                queue.append((nx, ny, dir, visited[x][y][dir]))
            elif graph[nx][ny] == "!":
                turn_clock = dir + 1
                turn_counter_clock = dir - 1
                if turn_clock == 4:
                    turn_clock = 0
                if turn_counter_clock == -1:
                    turn_counter_clock = 3

                # print("Appending ", (nx, ny, turn_clock, turn_counter_clock, num_mirror + 1))
                queue.append((nx, ny, dir, visited[x][y][dir]))
                if visited[nx][ny][turn_clock] == -1 or visited[nx][ny][turn_clock] >= visited[nx][ny][dir] + 1:
                    queue.append((nx, ny, turn_clock, visited[x][y][dir] + 1))
                if visited[nx][ny][turn_counter_clock] == -1 or visited[nx][ny][turn_counter_clock] >= visited[nx][ny][dir] + 1:
                    queue.append((nx, ny, turn_counter_clock, visited[x][y][dir] + 1))
                

print(ret)