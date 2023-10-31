"""
3
0 0 0
0 0 0
0 0 0

--> 1
"""

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))


# 0 1 2 , 오른쪽, 대각선, 왼쪽
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]

dp[0][0][1] = 1
for i in range(2, n):
    if graph[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]


for i in range(1, n):
    for j in range(1, n):

        # 대각선 파이프 경우에는 전 블록에 있던 가로, 대각선, 세로를 다확 인해야함 + 가는길에 벽이 없어야함
        if graph[i][j] == 0 and graph[i - 1][j] == 0 and graph[i][j - 1] == 0:
            dp[1][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]

        if graph[i][j] == 0:
            dp[0][i][j] = dp[0][i][j - 1] + dp[1][i][j - 1]
            dp[2][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]
        
ret = dp[0][n-1][n-1] + dp[1][n-1][n-1] + dp[2][n-1][n-1]
print(ret)






