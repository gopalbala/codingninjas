class PriorityQueueNode:
    def __init__(self, ele, priority):
        self.ele = ele
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.pq = []

    def isEmpty(self):
        return self.getSize() == 0

    def getSize(self):
        return len(self.pq)

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].ele

    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2

            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                self.pq[parentIndex], self.pq[childIndex] = self.pq[childIndex], self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break

    def insert(self, ele, priority):
        pqNode = PriorityQueueNode(ele, priority)
        self.pq.append(pqNode)
        self.__percolateUp()

    def __percolateDown(self):
        
        i = 0
        l = 2 * i + 1
        r = 2 * i + 2
        while l < self.getSize():
            if r < self.getSize() and self.pq[l].priority > self.pq[r].priority:
                eleToSwap = r
            else:
                eleToSwap = l
            if self.pq[i].priority < eleToSwap:
                break
            else:
                self.pq[i], self.pq[eleToSwap] = self.pq[eleToSwap], self.pq[i]
            i = eleToSwap
            l = 2 * i + 1
            r = 2 * i + 2

    def removeMin(self):
        if self.isEmpty():
            return None
        # Implment This Function Here
        n = self.getSize() - 1
        x = self.pq[0]
        self.pq[0] = self.pq[n]
        self.pq.pop()
        self.__percolateDown()
        return x.ele


myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i = 1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i += 1
        myPq.insert(element, element)
    elif choice == 2:
        print(myPq.getMin())
    elif choice == 3:
        print(myPq.removeMin())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i += 1
