"""

5
-2 4 -99 -1 98

4
0 0 5 5

4
1 2 3 4


5
-1 -2 -3 -4 -5


1 2 3 4 5

-99 -2 -1 4 98
0    1  2 3 4

두개의 합이 0에 제일 가깝도록


mid?

두개의 합을 start end라 정할 때




"""

n = int(input())
num_list = list(map(int, input().split()))

num_list.sort()
# print(num_list)

start_idx = 0
end_idx = len(num_list) - 1

min_diff = 2e9

ret = []

while start_idx < end_idx:
    sum = abs(num_list[start_idx] + num_list[end_idx])
    # print("FOR ", (num_list[start_idx], num_list[end_idx]), " we have ", sum)
    if sum < min_diff:
        min_diff = sum
        ret = [num_list[start_idx], num_list[end_idx]]
        if num_list[start_idx] + num_list[end_idx] == 0:
            break

    if num_list[start_idx] + num_list[end_idx] < 0:
        start_idx += 1
    elif num_list[start_idx] + num_list[end_idx] > 0:
        end_idx -= 1

    

print(ret[0], ret[1])


