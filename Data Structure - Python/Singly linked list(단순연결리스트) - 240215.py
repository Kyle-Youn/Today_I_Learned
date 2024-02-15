# 단순연결리스트 노드 구현
class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next



# 노드 테스트
first = Node(1)
second = Node(2)
third = Node(3)
first.next = second
second.next = third
first.value = 6





# 단순연결리스트 구현
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    # append구현 : 연결리스트 오른쪽 맨 끝에 노드 추가
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.next = new_node
            self.tail = new_node
        self.length += 1    
    
    # get구현 : 인덱스를 파라미터로 받아 해당 값 반환
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value
    
    # len구현 : 연결리스트의 길이 반환
    def __len__(self):                  #파이썬 매직메서드 : 문법의 일관성 유지
        return self.length
    
    # insert구현 : 인덱스를 파라미터로 받아 노드 추가
    def insert(self, idx, value):
        # 인덱스 범위 이탈 시
        if idx < 0 or idx > self.length:
            return "Index out of bounds"
        new_node = Node(value)
        # idx 0에 삽입할 때
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
            if self.length == 0:
                self.tail = new_node           
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            if idx == self.length:
                self.tail = new_node
        self.length += 1
        
    # remove구현 : 인덱스를 파라미터로 받아 노드 제거
    def remove(self, idx):
        # 인덱스 범위 이탈 시
        if 0 > idx and idx >= self.length:
            return "Index out of bounds"
        # 제거할 노드가 없을 시
        if self.length == 0:
            return "There are no nodes."
        
        if idx == 0:
            removed_node = self.head    # 제거될 노드
            self.head = self.head.next    # head를 다음 노드로 이동
            if self.length == 1:    # 만약 제거하려는 노드가 유일한 노드였다면 tail도 None으로 설정
                self.tail = None
        else:
            current = self.head
            previous = None
            for i in range(idx):
                if i == idx-1:
                    previous = current
                current = current.next
            removed_node = current     # 제거될 노드
            previous.next = current.next    # 이전 노드의 next를 제거될 노드의 다음 노드로 연결
            
            if idx+1 == self.length:    # 마지막 노드를 제거하는 경우, tail 업데이트
                self.tail = previous
        
        self.length -= 1
        return removed_node.value     # 제거된 노드의 값 반환 