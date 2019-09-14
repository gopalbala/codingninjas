class stack:
    def __init__(self):
        self.__size = 0
        self.__arr  = []
   
    def push(self,*data):
        self.__arr.append(data)
        self.__size = self.__size + 1
   
    def update(self,count):
        self.__arr[-1][1] = count
   
    def pop(self):
        if self.isEmpty():
            return None,0
        popdata = self.__arr[-1]
        self.__arr = self.__arr[:-1]
        self.__size = self.__size - 1
       
        return popdata
        
    def top(self):
        if self.isEmpty():
            return None,0
        else:
            return self.__arr[-1]
       
    def isEmpty(self):
        return self.__size == 0
    
    def getsize(self):
        return self.__size


def stockSpan(arr,n):
    lmax = [1]      
    s = stack()
    s.push(arr[0],1)
    for i in range(1,n):
        lcount = 1
        if not s.isEmpty():
            value, count = s.top()
            while value is not None and value < arr[i]:
                value, count = s.pop()
                lcount       = lcount + count
                if value is not None:
                    value, count = s.top()
            s.push(arr[i],lcount)
               
        else:
            s.push(arr[i],lcount)
        lmax.append(lcount)
       
    return lmax
                
        
#### Implement Your Code Here

n = int(input())
price = [int(ele) for ele in input().split()]
spans = stockSpan(price,n)
for ele in spans:
    print(ele,end= ' ')
