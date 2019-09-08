class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete(head, i):
    # A linked list and a position i, delete the node of ith position from
    # Linked List iteratively. If position i is greater than length of LL, then
    # you should return the same LL without any change. Indexing starts from 0.
    # You don't need to print the elements, just delete the node and return the
    # head of updated LL.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if i == 0:
        return head.next
    l = length(head)
    if i > l-1:
        return head
    temp = head
    count = 0
    while count < i-1:
        temp = temp.next
        count+=1
    
    if temp.next.next != None:
        temp.next = temp.next.next
    else:
        temp.next = None
        
    return head
    
def length(head):
    temp = head
    count = 0
    if temp is None:
        return count
    while temp is not None:
        count += 1
        temp = temp.next
    return count

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
i=int(input())
l = delete(l, i)
printll(l)
