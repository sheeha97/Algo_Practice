"""
백준 테트리스 게임 - 실패

테트리스 5가지 모양, 90도로 회전 가능
이때 각 테스트 케이스 마다 가장 큰 숫자 4의 합을 구하시오

모든 테트리스 조각의 모양은 4개로 이루어진 모든 모양이 가능, 그러므로 4개로 이어진 칸수의 조합 중에 가장 큰것을 return

"""
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
board = []


def dfs(n, x, y, depth, visited):
    if depth == 3:
        return board[x][y]
    max_val = 0
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if visited[nx][ny] == 1:
                continue
            visited[nx][ny] = 1
            print((nx, ny), " has been visited and the depth is: ", depth + 1)
            value = dfs(n, nx, ny, depth + 1, visited)
            visited[nx][ny] = 0
            max_val = max(max_val, value)
            
    print("The depth is :", depth, " and the ret value is ", board[x][y] + max_val)
    return board[x][y] + max_val

def main():
    global board
    while True:
        n = int(input())
        if n == 0:
            return
        board = []
        for _ in range(n):
            board.append(list(map(int, input().split())))
        
        for i in range(n):
            for j in range(n):
                visited = [[0 for _ in range(n)] for _ in range(n)]
                visited[i][j] = 1
                ret = dfs(n, i, j, 0, visited)
                visited[i][j] = 0
                print("At ", (i, j), " the largest sum is: ", ret)

main()