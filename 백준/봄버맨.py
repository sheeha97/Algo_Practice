"""
격자 안에 폭탄 or 빈칸

상하좌우 4칸 터짐 + 폭탄 있는 칸
폭발 연쇄 반응은 없음, 폭탄 터질 때 옆에 폭탄 있으면 파괴

봄버맨은 폭탄 면역

1. 봄버맨은 일부 칸에 폭탄 설치 (모든 폭탄은 설치 시간이 같다)
2. 다음 1초 동안 아무것도 안함
3. 다음 1초동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치한다 (모든 칸에 폭탄 설치)
4. 1초가 지난 후에 3초전에 설치된 폭탄이 모두 폭발한다.

3-4 반복

R, C, N


ex) 
6 7 3
.......
...O...
....O..
.......
OO.....
OO.....

-->
OOO.OOO
OO...OO
OOO...O
..OO.OO
...OOOO
...OOOO

6 7 6
.......
...O...
....O..
.......
OO.....
OO.....

6 7 7
.......
...O...
....O..
.......
OO.....
OO.....



6 7 1
.......
...O...
....O..
.......
OO.....
OO.....


"""

r, c, n = map(int, input().split())

board = []
full_bomb_board = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(r):
    line = list(input())
    board.append(line)
    bomb_line = list("O" * c)
    full_bomb_board.append(bomb_line)


def explode(board):
    full_bomb_map = [["O" for i in range(c)] for i in range(r)]

    for i in range(r):
        for j in range(c):
            if board[i][j] == "O":
                full_bomb_map[i][j] = "."
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx and nx < r and 0 <= ny and ny < c:
                        full_bomb_map[nx][ny] = "."

    return full_bomb_map

# print(full_bomb_board)
if n == 1:
    for i in range(r):
        print("".join(board[i]))
elif n % 2 == 0:
    for i in range(r):
        print("".join(full_bomb_board[i]))
else:
    exploded_board = []
    exploded_board = explode(board)

    if n % 4 == 3:
        for i in range(r):
            print("".join(exploded_board[i]))

    elif n % 4 == 1:
        exploded_board2 = []
        exploded_board2 = explode(exploded_board)
        for i in range(r):
            print("".join(exploded_board2[i]))