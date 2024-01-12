class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def mergeTwoLists(list1: [ListNode], list2: [ListNode]):
    #start with a dummy to reference the head
    #make a current to track the path
    dummy = ListNode()
    curr = dummy

    #as long as both list are not null then keep looping
    while list1 and list2:
        #compare values
        if list1.value < list2.value:
            curr.next = list1
            #move pointer on modified list to next item
            list1 = list1.next
        else: 
            curr.next = list2
            list2 = list2.next
        # make sure curr is on the next node just added
        curr = curr.next
    #when finished check if there are any remaining values in eihter linked list and point to its head
    if list1:
        curr.next = list1
    elif list2:
        curr.next = list2
        
    return dummy.next
#return head of list
    

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

mergeTwoLists(list1, list2)
