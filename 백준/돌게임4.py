"""
백준 돌게임
dp

돌은 1개 or 3개 or 4개 take 가능 
마지막 돌을 가져가는 사람이 패배

두사람이 완벽하게 게임 했을 때 승자?
상근이 먼저 한다


return sk or cy

sk == 1
cy == 0
"""

n = int(input())

win_list = [0 for _ in range(1001)]

# 상근이가 처음으로 움직이므로, 1개 일때 무조건 패배한다
win_list[1] = 0
win_list[2] = 1 # 이때는 창영이 무조건 패배
win_list[3] = 0 # 이 때는 상근이 다시 패배
win_list[4] = 1 # 이때 상근이 3개 가져가므로 창여의 패배


for i in range(5, n+1):
    # 
    if win_list[i - 1] == 0 or win_list[i - 3] == 0 or win_list[i - 4] == 0:
        win_list[i] = 1
    else:
        win_list[i] = 0


if win_list[n] == 1:
    print("SK")
else:
    print("CY")

