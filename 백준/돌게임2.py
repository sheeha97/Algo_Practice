"""
dp 연습

돌게임과 유사하나 마지막 돌을 먹는 사람이 진다

상근 승리 시 == 1 ret SK
창영 승리 시 == 0 ret CY

"""

n = int(input())

win_list = [0 for _ in range(1001)]

win_list[1] = 0 # 하나 밖에 없을 떄는 무조건 상근이의 패배 
win_list[2] = 1 # 두개 있을 씨 창영의 패배
win_list[3] = 0 # 다시 상근이의 패배
win_list[4] = 1 # 상근이가 3개를 가져갈 시 창영의 패배

for i in range(5, n + 1):
    if win_list[i - 3] == 1 or win_list[i -1] == 1:
        win_list[i] = 0
    else:
        win_list[i] = 1

if win_list[n] == 1:
    print("SK")
else:
    print("CY")
