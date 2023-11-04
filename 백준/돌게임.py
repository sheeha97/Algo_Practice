"""
백준 돌게임
dp

돌은 1개 or 3개 take 가능 
마지막 돌을 가져가는 사람이 승리

두사람이 완벽하게 게임 했을 때 승자?
상근이 먼저 한다


return sk or cy

sk == 1
cy == 0
"""

n = int(input())

win_list = [0 for _ in range(1001)]

# 상근이가 처음으로 움직이므로, 1 또는 3개로 시작할 때 무조건 이긴다
win_list[1] = 1
win_list[2] = 0 # 이떄만 창영이 이긴다
win_list[3] = 1

for i in range(4, n+1):
    # 창영이 이기는 경우에 수, 왜냐하면 그 전수는 상근이 했으므로
    if win_list[i - 1] == 1 or win_list[i - 3] == 1:
        win_list[i] = 0
    else:
        win_list[i] = 1


if win_list[n] == 1:
    print("SK")
else:
    print("CY")

