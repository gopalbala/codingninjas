import heapq

def findpos(arr,pos):
    heap = []
    for i in arr:
        heap.append(i)
    heapq._heapify_max(heap)
    i = 0
    count = 0
    while len(arr) > 0:
        if count == pos:
            return count
        if arr[0] >= heap[0]:
            count+=1
            heap.pop(0)
            arr.pop(0)
            heapq._heapify_max(heap)
            i+=1
        else:
            item = arr.pop(0)
            arr.append(item)
# n = int(input())
arr = [int(ele) for ele in input().split()]
idx = int(input())
res = findpos(arr,idx)
print(res)