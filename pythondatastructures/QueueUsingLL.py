
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class QueueUsingLL:
  
### Implement These Functions Here    
    def __init__(self):
        self.__node = None
        self.__head = None
        self.__tail = None
        self.__size = 0
        
    def enqueue(self,data):
        if self.__node is None:
            self.__node = Node(data)
            self.__head = self.__node
            self.__tail = self.__node
            self.__size = 1
        else:
            self.__tail.next = Node(data)
            self.__size = self.__size + 1
        
    def dequeue(self):
        if self.__head is None:
            return 0
        else:
            temp = self.__head
            self.__head = self.__head.next
            self.__size = self.__size - 1
            return temp.data
    
    def front(self):
        if self.__head is not None:
            return self.__head.data
        else:
            return 0
        
    def isEmpty(self):
        return self.__head is None
    
    def getSize(self):
        return self.__size

    
q = QueueUsingLL()
li = [int(ele) for ele in input().split()]
i=0
while i<len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        q.enqueue(li[i+1])
        i+=1
    elif choice == 2:
        ans = q.dequeue()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = q.front()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(q.getSize())
    elif choice == 5:
        if(q.isEmpty()):
            print('true')
        else:
            print('false')
    i+=1
