"""
CodeTree
산타의 선물 공장
벨트의 정보와 선물의 정보를 조회 할 수 있는 기능들을 추가

1. 공장 설립
n개의 벨트 설치
총 m개의 선물의 위차가 공백을 사이에 두고 주어짐


2. 물건 모두 옮기기
m_src번쨰 벨트에 있는 선물들을 모두 m_dst 벨트의 선물들로 옮깁니다.
옮겨진 선물들은 m_dst 벨트 앞에 위치합니다. if n_src번쨰 벨트에 선물이 존재 하지 않다면 아무것도 옮기지 않아도 됩니다.
옮긴 뒤에 m_dst번째 벨트에 있는 선물들의 개수를 출력합니다.

return 옮긴 뒤에 m_dst번쨰 벨트에 있는 선물들의 개수


3. 앞 물건만 교체하기
m_src번째 벨트에 있는 선물 중 가장 앞에 있는 선물을 m_dst번쨰 벨트의 선물 들 중 가장 앞에 있는 선물과 교체 합니다.
둘 중 하나의 벨트에 선물이 아예 존재 하 지 않다면 교체하지 않고 해달 벨트로 옮기기만 합니다.

return m_dst 번째 벨트에 있는 선물들의 개수


4. 물건 나누기
m_src번쨰 벨트에 있는 선물들의 개수를 n이라고 할 때 가장 앞에서 floor(n/2)번쨰 까지 있는 선물을 m_dst번째 벨트 앞으로 옮깁니다. 만약 m_src 벨트에 선물이 1개인 경우에는 선물을 옮기지 않습니다.
옮긴 뒤에 m_dst번쨰 벨트에 있는 선물들의 개수 출력


5. 선물 번호 p_num가 주어 질 때, 해당 선물의 앞 선물의 번호 a과 뒤 선물의 번호 b라 할때  @@ a + 2 * b @@ 출력합니다. 만약 앞 선물이 없는 경우에는 a=-1, 뒤 선물이 없는 경우에는 b=-1을 넣어 줍니다.


6. 벨트 번호 b_num이 주어 질 떄, 해당 벨트의 맨 앞에 있는 선물의 번호를 a, 맨 뒤에 있는 선물의 번호를 b, 해당 벨트에 있는 선물의 개수를 c라고 할때, a + 2*b + 3*c의 값을 출렵합니다.
    선물이 없는 벨트의 셩우에는 a와 b 모두 -1이 됩니다.

input:
q -> number of inputs
100 n m B_NUM1 B_NUM2 ... B_NUMm
200 m_src m_dst
300 m_src m_dst
400 m_src m_dst
500 p_num
500 b_num

ex)
8
100 4 6 1 2 2 2 1 4
200 2 4
300 2 4
400 4 2
500 6
500 5
600 1
600 3

"""

class Present:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class Belt:
    def __init__(self, data):
        self.data = data
        self.head = None
        self.tail = None
        self.size = 0


"""
n개의 벨트 설치
m개의 선물 제조 및 벨트에 배치

present_list example: 1 2 2 2 1 4

return list of belts and presents
"""
def initiate(n, m, p_list):
    belt_list = [Belt(None)]
    present_list = [Present(None)]

    # create n belts with their ids
    for b_num in range(1, n + 1):
        belt = Belt(b_num)
        belt_list.append(belt)
    
    # create m presents with their ids
    for p_num in range(1, m + 1):
        b_num = p_list[p_num - 1]
        present = Present(p_num)
        present_list.append(present)
        # 밸트의 첫번 째 선물
        if belt_list[b_num].head is None:
            belt_list[b_num].head = present
        
        # 그 이후로는 꼬리의 다음은 새로운 선물, 선물의 prev 는 (전) 꼬리
        else:
            belt_list[b_num].tail.next = present
            present.prev = belt_list[b_num].tail

        # 추가 되면 꼬리는 항상 바뀜
        belt_list[b_num].tail = present

        # 또한 벨트의 전체 크기를 track 합니다.
        belt_list[b_num].size += 1
    
    return belt_list, present_list


"""
m_src 벨트에 존재하는 모든 선물들을 m_dest 벨트로 옮깁니다
1. m_src에 있던 선물들이 앞에 가야 합니다
2. m_src.size == 0 그럼 아무것도 안해도 돕니다.
"""
def move_all_present(src_belt: Belt, dest_belt: Belt) -> None:
    # src_belt에 아무것도 없습니다.
    if src_belt.size == 0:
        return dest_belt.size
    
    src_first = src_belt.head
    src_last = src_belt.tail
    # dest_belt에 아무것도 없을 경우 simply copy
    if dest_belt.head is None:
        dest_belt.tail = src_last
    # 있는 경우
    else:
        dest_first = dest_belt.head
        src_last.next = dest_first
        dest_first.prev = src_last
    

    # src_belt에 있던 정보들을 지웁니다.
    dest_belt.size += src_belt.size
    dest_belt.head = src_first
    src_belt.size = 0
    src_belt.head = None
    src_belt.tail = None

    return dest_belt.size


"""
m_src 벨트와 m_dest의 첫번 쨰 선물을 서로 교환 합니다
1. 둘 중 하나라도 없으면 그냥 옮깁니다.
"""
def switch_present(src_belt: Belt, dest_belt: Belt) -> None:
    if src_belt.size == 0 and dest_belt.size == 0:
        return 0
    
    # src가 없는 경우
    if src_belt.size == 0:
        src_belt.head = dest_belt.head
        src_belt.tail = dest_belt.head
        # dest가 노드가 하나보다 더 많을 경우
        if dest_belt.head.next is not None:
            dest_belt.head.next.prev = None
            dest_belt.head = dest_belt.head.next
        # 하나 밖에 없을 경우 꼬리도 지정
        else:
            dest_belt.head = None
            dest_belt.tail = None
        dest_belt.size -= 1
        src_belt.size += 1
        src_belt.head.next = None
    
    # dest가 없는 경우
    elif dest_belt.size == 0:
        dest_belt.head = src_belt.head
        dest_belt.tail = src_belt.head

        # 하나보다 더 많을 경우
        if src_belt.head.next is not None:
            src_belt.head.next.prev = None
            src_belt.head = src_belt.head.next
        # 하나 밖에 없을 경우 꼬리도 지정
        else:
            src_belt.tail = None
            src_belt.head = None

        src_belt.size -= 1
        dest_belt.size += 1
        dest_belt.head.next = None

    # 둘다 있는 경우
    else:
        # 첫번째
        src_first = src_belt.head
        dest_first = dest_belt.head

        src_first_next = src_first.next
        dest_first_next = dest_first.next

        # 먼저 head pointer 부터 바꿔 줍니다
        src_belt.head = dest_first
        dest_belt.head = src_first

        # present 들 간의 포인터 정리를 해줍니다 (next 와 prev)
        src_first.next = dest_first_next
        dest_first.next = src_first_next

        # 최소 두개 일 경우
        if src_first_next is not None:
            src_first_next.prev = dest_first
        # 한개 만 존재하면
        else:
            src_belt.tail = src_belt.head
        
        if dest_first_next is not None:
            dest_first_next.prev = src_first
        else:
            dest_belt.tail = dest_belt.head

    return dest_belt.size


"""
m_src번쨰 벨트에 있는 선물들의 개수를 n이라고 할 때 가장 앞에서 floor(n/2)번쨰 까지 있는 선물을 m_dst번째 벨트 앞으로 옮깁니다. 
1. 만약 m_src 벨트에 선물이 1개인 경우에는 선물을 옮기지 않습니다.
return : 옮긴 뒤에 m_dst번쨰 벨트에 있는 선물들의 개수 출력
"""
def divide_present(src_belt: Belt, dest_belt: Belt) -> None:
    if src_belt.size <= 1:
        return dest_belt.size

    src_size = src_belt.size
    num_to_move = src_size // 2

    src_first = src_belt.head
    cur = src_belt.head
    dest_first = dest_belt.head
    new_head = None

    # 옮겨야 되는 곳으로 움직입니다.
    for _ in range(num_to_move - 1):
        cur = cur.next
    new_head = cur.next
    # 이제 이어 줍니다.
    # 비어 있을경우
    if dest_belt.size == 0:
        dest_belt.tail = cur
    # 비어 있지 않음
    else:
        cur.next = dest_first
        dest_first.prev = cur
    
    # 소스의 새로운 헤드는 prev 가 없습니다.
    src_belt.head = new_head
    src_belt.head.prev = None
    dest_belt.size += num_to_move

    # 고침
    cur.next = dest_belt.head

    dest_belt.head = src_first
    src_belt.size -= num_to_move
    

    return dest_belt.size

"""
선물의 정보를 출력 합니다
정보는 :  a + 2 * b
1. prev 가 없으면 a = -1
2. next 가 없으면 b = -1
"""
def get_present_info(present: Present) -> int:
    a = 0
    b = 0
    if present.prev is None:
        a = -1
    else:
        a = present.prev.data
    
    if present.next is None:
        b = -1
    else:
        b = present.next.data

    return (a + 2 * b)


"""
선물들의 정보를 출력 합니다
정보는 :  a + 2*b + 3*c
1. a = 맨 앞 선물 정보
2. b = 맨 뒤 선물 정보
3. c = 벨트 총 선물 수  
4. 선물 없으면 a, b == -1
"""
def get_belt_info(belt: Belt) -> int:
    a, b, c = 0, 0, 0
    c = belt.size
    if c == 0:
        a = -1
        b = -1
    else:
        a = belt.head.data
        b = belt.tail.data

    return a + 2 * b + 3 * c

    

        
def tester(belt_list, present_list):
    for belt in belt_list:
        if belt.data is not None:
            print("Belt info: ", belt.data)
            if belt.head is not None:
                print("Head is ", belt.head.data)
            if belt.tail is not None:
                print("Tail is ", belt.tail.data)
            print("Belt size is ", belt.size)

    for present in present_list:
        if present.data is not None:
            print("Present info: ", present.data)
            if present.next is not None:
                print("Next is ", present.next.data)
            if present.prev is not None:
                print("Prev is ", present.prev.data)


def main():
    belt_list = []
    present_list = []
    q = int(input())
    for _ in range(q):
        line = list(map(int, input().split()))
        func_type = line[0]
        if func_type == 100:
            n = line[1]
            m = line[2]
            p_list = line[3:len(line)]
            belt_list, present_list = initiate(n, m , p_list)
            # tester(belt_list, present_list)

        elif func_type == 200:
            m_src = line[1]
            m_dest = line[2]
            print(move_all_present(belt_list[m_src], belt_list[m_dest]))
            # tester(belt_list, present_list)

        elif func_type == 300:
            m_src = line[1]
            m_dest = line[2]
            print(switch_present(belt_list[m_src], belt_list[m_dest]))
            # tester(belt_list, present_list)

        elif func_type == 400:
            m_src = line[1]
            m_dest = line[2]
            print(divide_present(belt_list[m_src], belt_list[m_dest]))
            # tester(belt_list, present_list)

        elif func_type == 500:
            present = present_list[line[1]]
            print(get_present_info(present))
        elif func_type == 600:
            belt = belt_list[line[1]]
            print(get_belt_info(belt))

        else:
            print("Uknonw function type found: ", func_type)
            return -1
        

            
               


main()
