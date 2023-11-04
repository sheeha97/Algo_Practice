"""
퇴사
n+1 day 떄 퇴사
dynamic programming

T_i = 상담을 끝내는데 걸리는 시간
p_i = 금액

그럼 최대로 벌수 있는 amount를 계산 하시오

ex) 
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

--> 45
"""

n = int(input())
time_list = [0]
money_list = [0]
for _ in range(n):
    time, money = map(int, input().split())
    time_list.append(time)
    money_list.append(money)

dp = [0 for _ in range(n + 2)]
max_value = 0
# i는 현 시간으로 거구로 갑니다.
for i in range(n, -1, -1):
    # 당일 날에 시작하면 끝날떄까지 걸리는 시간
    time = time_list[i] + i

    # 오직 시간 내에 끝날 때만 합니다.
    if time <= n + 1:
        dp[i] = max(money_list[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
    print("This is DP : ", dp)
print(dp[0])