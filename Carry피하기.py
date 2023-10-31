"""
Code Tree
BACK-TRACKING EXAMPLE

7
40112404
3500062
10321011
10030160
4000103
20012220
14003000

7
40112404
3500062
10321011
10030160 **
4000103
20012220
14003000

20
41023233
40112404
3500062
1039625
700106
10321011
4554386
10494000
85859886
10030160
50020140
25003000
4000103
48311200
11053700
20012220
2433571
16026990
36892320
14003000




"""
n = int(input())

num_list = []

for _ in range(n):
    num_list.append(int(input()))



def check_carry(num_1, num_2):
    num_1 = str(num_1)
    num_2 = str(num_2)

    size_1 = len(num_1)
    size_2 = len(num_2)

    min_length = min(size_1, size_2)

    for i in range(min_length):
        temp_1 = int(num_1[size_1 - 1 - i])
        temp_2 = int(num_2[size_2 - 1 - i])

        if temp_1 + temp_2 >= 10:
            return False
    
    return True


def compare(num, idx, numbers):
    if idx == n:
        return numbers
    if not check_carry(num, num_list[idx]):
        return compare(num, idx + 1, numbers)
    else:
        # print(num_list[idx])
        temp_1 = compare(num + num_list[idx], idx + 1, numbers + [num_list[idx]])
        temp_2 = compare(num, idx + 1, numbers)
        if len(temp_1) > len(temp_2):
            return temp_1
        return temp_2


def main():
    max_carry = 0
    for i in range(n):
        num = num_list[i]
        numbers = compare(num, i + 1, [num])
        if len(numbers) > max_carry:
            max_carry = len(numbers)
            # print("The max number ", len(numbers))
            # print(numbers)
        
    return max_carry

print(main())