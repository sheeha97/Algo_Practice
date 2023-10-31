"""



3 10
10
20
15
"""



n, k = map(int, input().split())

num_list = []
# largest = 0
lowest = 1e9
for i in range(n):
    num = int(input())
    # largest = max(num, largest)
    num_list.append(num)
    lowest = min(num, lowest)

end = k + lowest
start = lowest

num_list.sort()
res = 0

while start <= end:
    mid = (start + end) // 2
    counter = 0
    # print("DEBUG: ", mid, start, end)
    for num in num_list:
        if mid > num:
            counter += (mid - num)
    
    # print("DEBUG: ", mid, counter)

    if counter <= k:
        start = mid + 1
        res = max(mid, res)
    else:
        end = mid - 1
        
    
print(res)




