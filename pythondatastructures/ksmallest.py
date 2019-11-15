import heapq


def ksmallest(arr,k):
    n = len(arr)
    heap = arr[:k]
    heapq._heapify_max(heap)
    
    for i in range(k,n):
        if heap[0] > arr[i]:
            heapq._heapreplace_max(heap,arr[i])
    return heap

arr = [10,6,7,2,3,8,9,11,1]

k = 4
elements = ksmallest(arr,k)
for ele in elements:
    print(ele, end = " ")