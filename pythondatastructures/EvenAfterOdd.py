# Problem ID 331 even after odd in a LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def arrange_LinkedList(head):
    #  Even after Odd LinkedList: Arrange elements in a given Linked List such
    #  that, all even numbers are placed after odd numbers. Respective order of
    #  elements should remain same.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    evenHead = None
    evenFirst = None
    oddFirst = None
    oddHead = None
    if head is None:
        return head
    while head is not None:
        if head.data % 2 > 0:
            if oddFirst is None:
                oddFirst = head
                oddHead = oddFirst
            else:
                oddHead.next = head
                oddHead = head
        else:
            if evenFirst is None:
                evenFirst = head
                evenHead = evenFirst
            else:
                evenHead.next = head
                evenHead = head
        head = head.next
    
    if evenFirst is not None:
        evenHead.next = None
    
    if oddFirst is None:
        return evenFirst
    else:
        oddHead.next = evenFirst
        return oddFirst
    

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = arrange_LinkedList(l)
printll(l)
