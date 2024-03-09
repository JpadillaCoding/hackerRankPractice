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

def isPalindrome(self, head: Optional[ListNode]) -> bool:
    slow = head
    fast = head
    prev = None

    if head is None or head.next is None:
        return True

    while fast and fast.next:
        fast = fast.next.next
        #track next
        nxt = slow.next
        #slow.next points to previous
        slow.next = prev
        # prev will now be the curr
        prev = slow
        # curr.next is now next
        slow = nxt

    if fast:
        slow = slow.next
    print(prev)
    print(slow)
    while slow and prev:
        if prev.val != slow.val:
            return False
        prev = prev.next
        slow = slow.next

    return True

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow

def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    slow = head
    fast = head.next
    prev = None

    while fast and fast.next:
        # find the middle, being slow
        fast = fast.next.next
        slow = slow.next

    while slow:
        # flip the node
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    head1 = head
    head2 = prev
    while head1 and head2:
        tempHead1 = head1.next
        tempHead2 = head2.next
        
        head1.next = head2
        head2.next = tempHead1
        
        head1 = tempHead1
        head2 = tempHead2
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # edge case of single
    if not head.next:
        if n == 1:
            head = None
            return head
    # find end of list while reversing
    curr = head
    rev = None
    while curr:
        nxt = curr.next
        curr.next = rev
        rev = curr
        curr = nxt
    # once at end then itierate by index of 1 to find nth node
    # as loop is iterating backwards, reflip the node pointer
    curr = None
    # make the flip before on the nth node
    if n == 1:
        temp = rev.next
        rev = None
        rev = temp
        n = n - 1
    while rev:
        n = n - 1
        # do logic to remove
        if n == 1:
            # edge case of nth node being last itieration
            if rev.next.next == None:
                rev.next = curr
                return rev
            else:
                rev.next = rev.next.next
        nxt = rev.next
        rev.next = curr
        curr = rev
        rev = nxt
    return head
def removeNthFromEndOPTIMIZED(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    fast = slow = head
    prev = None
# case of single node 
    if not head.next:
        head = None
        return head
# make the gap between slow and fast
    while n > 0:
        fast = fast.next
        n = n - 1
# move fast to final LL node along with keeping the gap with slow
    while fast:
        fast = fast.next
        prev = slow
        slow = slow.next
# Remove target node(slow) by using prev
    if not prev:
        # handle case of the node to remove being first the node in the LL
        head = slow.next
    else:
        prev.next = slow.next
    return(head)
def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    oldToCopy = {None: None}
    curr = head

    while curr:
        copy = Node(curr.val)
        oldToCopy[curr] = copy
        curr = curr.next

    curr = head
    while curr:
        copy = oldToCopy[curr]
        copy.next = oldToCopy[curr.next]
        copy.random = oldToCopy[curr.random]
        curr = curr.next
    return oldToCopy[head]
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
    