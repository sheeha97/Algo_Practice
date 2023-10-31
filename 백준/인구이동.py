"""
백준 : 인구 이동
if 국경선 open repeat
1. if 인구차이 L 이상 R 이하 then 국경 open
2. if 국경선 open 인구 이동
3. 국경선이 열려있있으면 연합
4. 연합의 각 칸 인구수 = 연합 인구수 / 연합 칸
5. 연합 해체
ex)
3 5 10
10 15 20
20 30 25
40 22 10

--> 2


# 배울 점: 
1.
import sys
sys.setrecursionlimit(10 ** 6)

2. 
N * N 일 때 제발 새로운 리스트 또만들지 마

"""
import sys
sys.setrecursionlimit(10 ** 6)

graph = []
visited = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
counter = 0
n, l, r = map(int, input().split())

for _ in range(n):
    graph.append(list(map(int, input().split())))

def check(x, y):
    if 0 <= x and x < n and 0 <= y and y < n:
        return True
    return False


def move_population(union):
    size = len(union)
    total_pop = 0
    for country in union:
        x, y = country
        total_pop += graph[x][y]
    new_pop = total_pop // size

    for country in union:
        x, y = country
        graph[x][y] = new_pop


def dfs(x, y):
    # mark as visited
    visited[x][y] = 1
    pop = graph[x][y]
    ret = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if check(nx, ny) and visited[nx][ny] == 0:
            diff = abs(pop - graph[nx][ny])
            # union check
            if l <= diff and diff <= r:
                ret = ret + dfs(nx, ny)
                union_check[nx][ny] = 1
        
    return [(x, y)] + ret

counter = 0
while True:
    all_union = []
    visited = [[0 for _ in range(n)] for _ in range(n)]
    union_check = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if union_check[i][j] == 1:
                continue
            union = dfs(i, j)
            if len(union) > 1:
                union_check[i][j] == 1
                all_union.append(union)

    if len(all_union) == 0:
        break
    else:
        for union in all_union:
            move_population(union)
    counter += 1

print(counter)






