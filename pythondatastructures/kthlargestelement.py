import heapq
def kthLargest(lst, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    # heap = lst[:k]
    # heapq._heapify_max(heap)
    # n = len(lst)

    # for i in range(k,n):
    #     if heap[0] > lst[i]:
    #         heapq.heapreplace(heap,lst[i])
    # return heap[k-1]
    heap = []
    for elem in lst:
        if len(heap) < k:
            heapq.heappush(heap,elem)
        else:
            heapq.heappushpop(heap,elem)
    if len(heap) < k:
        return 0
    else:
        return heap[0]
    
# Main Code
# n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)

