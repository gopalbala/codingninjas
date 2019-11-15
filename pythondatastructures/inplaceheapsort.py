
def heapSort(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        downHeapify(arr, i, n)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        downHeapify(arr, 0, i)
    return arr

def downHeapify(arr, i, n):
    parentIndex = i
    lci = 2 * i + 1
    rci = 2 * i + 2
    while lci < n:
        swapindex = parentIndex
        if arr[lci] < arr[swapindex]:
            swapindex = lci
        if rci < n and arr[rci] < arr[swapindex]:
            swapindex = rci
        if swapindex == parentIndex:
            return
        arr[parentIndex], arr[swapindex] = arr[swapindex], arr[parentIndex]
        parentIndex = swapindex
        lci = 2 * parentIndex + 1
        rci = 2 * parentIndex + 2
    return

arr = [int(ele) for ele in input().split()]
heapSort(arr)
print(*arr)