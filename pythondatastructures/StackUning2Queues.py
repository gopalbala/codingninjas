
import queue
class StackUsingQueues:
    
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        
    def push(self,data):
        if self.q1 is None:
            self.q1 = queue.Queue()
        self.q1.put(data)
        while self.q2.qsize() > 0:
            self.q2.get()
        self.q2.put(data)

    def pop(self):
        if self.q2.qsize() == 0:
            return 0
        else:
            data = self.q2.get()
            last = 0
            while self.q1.qsize() > 1:
                last = self.q1.get()
                self.q2.put(last)
            while self.q1.qsize() > 0:
                self.q1.get()
            self.q1.put(last)
            self.q1, self.q2 = self.q2, self.q1
            return data
    
    def top(self):
        if self.q2.qsize() > 0:
            data = self.q2.get()
            self.q2.put(data)
            return data
        else:
            return 0
        
    def getSize(self):
        return self.q1.qsize()
    
s = StackUsingQueues()
li = [int(ele) for ele in input().split()]
i=0
while i<len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        s.push(li[i+1])
        i+=1
    elif choice == 2:
        ans = s.pop()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = s.top()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(s.getSize())
    elif choice == 5:
        while s.q1.qsize() !=0:
            print(s.q1.get(),end=' ')
            
    i+=1

    # 3,4,63,21,