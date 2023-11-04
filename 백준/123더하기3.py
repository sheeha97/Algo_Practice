"""
백준 123 더하기 3


정수 4를 1,2,3 합으로 나타내는 방법 7가지

1111
112
121
211
22
13
31


3
111
12
21
3



3
4
7
10
"""



n = int(input())

sum_list = [0 for i in range(int(1e6+1))]

sum_list[1] = 1
sum_list[2] = 2
sum_list[3] = 4

for i in range(4, int(1e6+1)):
    sum_list[i] = (sum_list[i-3] + sum_list[i - 1] + sum_list[i - 2]) % int(1e9+9)

for _ in range(n):
    num = int(input())
    print(sum_list[num])


