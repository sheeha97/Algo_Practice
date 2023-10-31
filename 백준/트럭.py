"""
백준 13335번 시물레이션

- 다리를 n개의 트럭이 건넘
- 순서 바꾸기 x
- 무게는 서로 같지 않을 수 있다
- w대의 트럭만 동시에 이동 가능
- 다리의 길이는 w 단위 길이 
- 각 트럭들은 하나의 단위 길이 만큼 이동 가능
- **동시에 다리 위에 올라가 있는 트럭들의 무게 sum  <= L

constraints 
n (1 ≤ n ≤ 1,000) , w (1 ≤ w ≤ 100) and L (10 ≤ L ≤ 1,000)

n, w, l
[트럭의 무게 list]

ex)
4 2 10
7 4 5 6

--> 8

"""
from collections import deque


# input
n, w, l = map(int, input().split())
truck_list = list(map(int, input().split()))

# var
time = 1
cur_weight = 0
truck_q = deque(truck_list)
cur_weight = truck_q.popleft()
bridge_q = deque([(cur_weight, time)])

# print(bridge_q[0])

while bridge_q:
    time += 1
    first_truck = bridge_q[0]
    
    # this is the case when the truck leaves the bridge
    if time - first_truck[1] >= w:
        cur_weight -= first_truck[0]
        bridge_q.popleft()
        # print("The cur time is ", time, " and truck left the bridge: ", first_truck)

    # if the the bridge can handle the weight add it
    if truck_q: 
        if cur_weight + truck_q[0] <= l:
            temp_weight = truck_q.popleft()
            bridge_q.append((temp_weight, time))
            cur_weight += temp_weight
            # print("The cur time is ", time, " and new truck is added : ", bridge_q[-1])


print(time)
    





