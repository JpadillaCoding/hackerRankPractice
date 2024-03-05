class Node:
    def __init__(self, data=0, next=None) -> None:
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

    def print(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next

def merge(list1, list2):
    dummy = Node()
    curr = dummy

    while list1.head and list2.head:
        if list1.head.data < list2.head.data:
            curr.next = list1.head
            list1.head = list1.head.next
        else:
            curr.next = list2.head
            list2.head = list2.head.next
        curr = curr.next
    if list1.head:
        curr.next = list1.head
    else:
        curr.next = list2.head

    return dummy.next

def hasCycle(self, head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
def removeElement(head, val):
    current = head
    
    if current is None:
        return head

    while current and current.next:

        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next

    if head.val == val:
        head = head.next
    return head

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # make a anchor pointer to track the item before
    # while curr is valid, reverse the pointer to the anchor

    anchor = None

    curr = head

    while curr:
        nxt = curr.next
        curr.next = anchor
        anchor = curr
        curr = nxt
    return anchor
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

list1.print()
list2.print()

merge(list1,list2)



""" def mergeTwoLists(self, list1, list2): """
    