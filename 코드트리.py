from collections import deque
"""
m = number of ppl
1번 사람은 1분
2번 사람은 2분
...
m번 사람은 m분에 각자의 베이스 캠프에서 출발

사람들이 목표로 하는 편의점은 모두 다릅니다. 
n * n board

3가지 행동이 1분 동안 진행 *** in order
1. everyone in the board -> conv_store direction 1칸 (shortest distance), 상하좌우, 이동 가능한 칸 (최단거리로 이동하는 방법 순서 (up, left, right, down))
2. if 편의점에 도착 stop -> 해당 칸은 blocked ***그 턴에 모든 격자 내 사람들이 이동 후에 blocked
3. if cur_time == t where t <= m then t번 사람은 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스 캠프에 들어감
    3.1 if min dist is the same, set basee camp as smaller row if same, set at smaller col
    3.2 t번 사람이 베이스 캠프로 이동하는 데이는 시간 x

at this point, 다른 사람들은 해당 베이스 캠프가 있는 칸 blokced. t번 사람이 편의점을 향해 가도 베이스 캠프: blocked
** also 그 턴에 모든 격자 내 사람들이 이동 후에 blocked

ex)
5 3
0 0 0 0 0
1 0 0 0 1
0 0 0 0 0
0 1 0 0 0
0 0 0 0 1
2 3
4 4
5 1


--> 7


"""
FIND_BASE = 1
FIND_NEXT = 2


n, m = map(int, input().split())
graph = []
stores = []
# camps = []
# cuz for now we are doing it backward
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# Once the person finds its store, STOP also define a variable to keep track of its current location
finished = {}
current_position = {}
for i in range(m):
    finished[i + 1] = False
    current_position[i + 1] = (0, 0)


# padding for 편안함
graph.append([0 for _ in range(n)])
for i in range(1, n + 1):
    line = list(map(int, input().split()))
    line.insert(0, 0)
    graph.append(line)

stores.append(())
for _ in range(m):
    x, y = map(int, input().split())
    stores.append((x, y))

"""
편의점을 향해 한 칸 가까이 움직입니다. (최단거리를 이용해)
"""
def move(p):
    cur_x, cur_y = current_position[p]
    # print("P는 ", p, " 움직이기 전 수는 ", (cur_x, cur_y))
    next_x, next_y = bfs(p, FIND_NEXT, cur_x, cur_y)
    current_position[p] = (next_x, next_y)
    # print("P는 ", p, " 움직인 수는 ", (next_x, next_y))


"""
편의점에 도착한 사람들은 멈추고 그 grid를 막습니다.
"""
def check_finished(p):
    cur_x, cur_y = current_position[p]
    if stores[p] == (cur_x, cur_y):
        graph[cur_x][cur_y] = 2
        finished[p] = True
        # print("끝남!! 그것은 바로 ", p)
        return True
    return False

"""
사람을 base camp에다 place 하는 function

arg p : 사람 번호
"""
def initiate(p):
    
    store_x, store_y = stores[p]

    # bfs를 이용해 최단 거리  base camp search
    camp_x, camp_y = bfs(p, FIND_BASE, store_x, store_y)
    graph[camp_x][camp_y] = 2
    current_position[p] = (camp_x, camp_y)
    # print("P는 ", p, " camp는 ", (camp_x, camp_y))

"""
type = 1
    bfs를 이용해 최단거리 base camp 를 찾습니다.

type = 2
    bfs를 이용해 최단거리 base camp를 가는 next move를 찾습니다

"""
def bfs(p, func_type, start_x, start_y):
    prev = {}
    queue = deque([(start_x, start_y)])
    visited = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    # print("Run Function for ", func_type, "and value is ", (start_x, start_y))
    while queue:
        x, y = queue.popleft()

        #by design dfs discovers the shortest path
        
        # return base camp grid
        if func_type == FIND_BASE:
            if graph[x][y] == 1:
                # print("INIT FOUND IT and x, y is ", (x, y))
                return (x, y)
        # run the path function to find the next move
        elif func_type == FIND_NEXT:
            if stores[p][0] == x and stores[p][1] == y:
                break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not check(nx, ny):
                continue
            elif graph[nx][ny] == 2:
                continue
            elif visited[nx][ny] == 0:
                # print("The nx ny is ", (nx, ny), "x y was ", (x, y))
                queue.append((nx, ny))
                # print("Queue is ", queue)
                visited[nx][ny] = 1
                prev[(nx, ny)] = (x, y)

        """
        최단 거리를 찾았으면 
        """
    # print("이제 path를 ", (x, y), " 에서부터 찾을 차래")
    def path(r, c):
        # 맨 앞 path를 찾는 function
        while r != start_x or c != start_y:
            prev_r, prev_c = prev[(r,c)]
            # print("Prev of ", (r, c), " is ", (prev_r, prev_c))
            if prev_r == start_x  and prev_c == start_y:
                # print("Done we found the next one.")
                # print("Which is ", (r, c))
                break
            else:
                r = prev_r
                c = prev_c
        
        return (r, c)

    return path(x, y)

"""
simple function to check if its within the graph
"""
def check(x, y):
    if 0 < x and x <= n and 0 < y and y <= n:
        return True
    return False


def main():
    # return 할 값
    time = 0
    # 모든 플레이어가 완료 되는 그날까지
    finish_counter = 0
    while finish_counter < m:
    #while time < 10:
        time += 1
        # 1. 모든 플레이어가 스토어 방향으로 1칸 이동(bfs) (shortest distance)
        for i in range(1, m + 1):
            # 이동하는 것은 person_num이 time 보다 커야 한다
            if i < time:
                if not finished[i]:
                    # print("Move ", i, " and the time is ", time)
                    move(i)
        
        # 2. if 편의점에 도착 stop -> 해당 칸은 blocked ***그 턴에 모든 격자 내 사람들이 이동 후에 blocked
        for i in range(1, m + 1):
            if i < time:
                if not finished[i]:
                    if check_finished(i):
                        finish_counter += 1
                        # print("현재 카운터는 ", finish_counter, " 그리고 m은 ", m)

        # 3. if cur_time == t where t <= m then t번 사람은 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스 캠프에 들어감 (이것도 bfs)
        # 3.1 if min dist is the same, set base camp as smaller row if same, set at smaller col
        # 3.2 t번 사람이 베이스 캠프로 이동하는 데이는 시간 x
        if time <= m:
            # print("Initiate ", time)
            initiate(time)
            # print("END Initiate")
    
    return time

ret = main()
print(ret)