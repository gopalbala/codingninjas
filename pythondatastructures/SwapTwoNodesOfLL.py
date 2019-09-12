class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_nodes(head, i, j):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if i == 0 or j == 0:
        return head
    if i == j:
        return head
    l = length(head)
    temp = head
    start = 0
    end = 0
    stNode = None
    edNode = None
    count = 0
    while count < l:
        if i == start:
            stNode = temp
        if j == end:
            edNode = temp
        start+=1
        end+=1
        count +=1
        temp = temp.next
    t = stNode.data
    stNode.data = edNode.data
    edNode.data = t
    return head
    
def length(head):
    temp = head
    l = 0
    if temp is None:
        return l
    while temp is not None:
        l += 1
        temp = temp.next
    return l

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
i, j=list(int(i) for i in input().strip().split(' '))
l = swap_nodes(l, i, j)
printll(l)
