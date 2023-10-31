"""




9 3
1 2 3 4 5 6 7 8 9

10 5
10000 10000 10000 10000 10000 10000 10000 10000 10000 10000


7 7
5 9 6 8 7 7 5

"""


n, m = map(int, input().split())

lessons = list(map(int, input().split()))

start = 0
end = 0
for i in range(len(lessons)):
    if lessons[i] > start:
        start = lessons[i]
    end += lessons[i]

while start <= end:
    mid = (start + end) // 2

    # print(start, end, mid)

    sub_total = 0
    blue_ray_count = 0
    for lesson in lessons:
        if sub_total + lesson > mid:
            blue_ray_count += 1
            sub_total = 0

        sub_total += lesson
    
    if sub_total != 0:
        blue_ray_count += 1

    if blue_ray_count <= m:
        end =  mid - 1
    else:
        start = mid + 1

print(start)
            
            



