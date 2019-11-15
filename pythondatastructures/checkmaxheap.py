import heapq
def checkMaxHeap(lst):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if len(lst) == 1:
        return True
    parent = 0
    lc = 1
    rc = 2
    n = len(lst)
    while lc < n:
        if lst[parent] < lst[lc]:
            return False
        if rc < n and lst[parent] < lst[lc]:
            return False
        parent += 1
        lc = 2 * parent + 1
        rc = 2 * parent + 2
    return True

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')