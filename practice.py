class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def mergeTwoLists(list1: [ListNode], list2: [ListNode]):
# needs to be sorted
# return the head of the new one
    # traverse list 
    # if list1[i] > list2[i]:
        # move list2[i] next to head of list1[i] 
    # elif move list1[i] next to head of list2[i]
    # else just do the if 
    # consider the fact one list can run out and the other doesn't
    dummy = ListNode(0)
    tail = dummy
    while list1 and list2:
        if list1.value < list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    return dummy.next

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

mergeTwoLists(list1, list2)
