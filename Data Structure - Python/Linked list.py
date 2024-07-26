class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # tail 노드 추가

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node  # 비어있는 리스트라면 head와 tail 모두 새 노드를 가리킴
            return
        self.tail.next = new_node  # 리스트의 마지막 노드의 next를 새 노드로 설정
        self.tail = new_node  # tail을 새 노드로 업데이트

    # 다른 메서드들...


    def print_list(self):
        """리스트의 모든 요소를 출력합니다."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()

    def prepend(self, data):
        """리스트 시작 부분에 새 노드를 추가합니다."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        """주어진 키를 가진 노드를 삭제합니다."""
        current_node = self.head

        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev.next = current_node.next
        current_node = None
