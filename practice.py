class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node


node1 = Node(1)
node2 = Node(2)
node3 = Node(4)
node4 = Node(1)
node5 = Node(3)
node6 = Node(4)

list1 = LinkedList(node1)
list1.append(node2)
list1.append(node3)

list2 = LinkedList(node4)
list2.append(node5)
list2.append(node6)