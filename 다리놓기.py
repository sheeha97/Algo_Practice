"""
사이트 == 다리를 지을수 있는곳

왼쪽에 n 개의 사이트
오른쪽에  m개의 사이트
n <= m

겹치는거 x
지을수 있는 다리 n개 그럼 경우의 수는?


ex)
4
2 2
1 5
13 29
14 30

"""
def factorial(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num

t = int(input())
ret_list = []
for _ in range(t):
    total = 1
    n, m = map(int, input().split())
    total = factorial(m) // (factorial(n) * factorial(m - n))
    ret_list.append(total)

for total in range(ret_list):
    print(total)
 


