class stack:
    def __init__(self):
        self.__size = 0
        self.__arr  = []
        self.__flag = []
   
    def push(self,data,flag):
        self.__arr.append(data)
        self.__flag.append(flag)
        self.__size = self.__size + 1
   
    def updateFlag(self,flag):
        if flag:
            self.__flag[-1] = True
        else:
            self.__flag[-1] = False
    
    def pop(self):
        if self.isEmpty():
            return None
        popdata = self.__arr[-1]
        popflag = self.__flag[-1]
        self.__arr = self.__arr[:-1]
        self.__flag = self.__flag[:-1]
        self.__size = self.__size - 1
       
        return popdata, popflag 
        
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.__arr[-1], self.__flag[-1]
       
    def isEmpty(self):
        return self.__size == 0
    
    def getsize(self):
        return self.__size


def checkRedundant(string):
    s1 = stack()
    for s in string:
        if s == "(" and s1.top() is not None:
            x, y = s1.top()
            if y:
                return True
            else:
                s1.push(s, True)
        elif s == "(" and s1.top() is None:
            s1.push(s,True)
        elif s == ")":
            x, y = s1.pop()
            if y:
                return True
            if x != "(":
                return False
        elif s != ' ' and s != '':
            if s1.top() is not None:
                x, y = s1.pop()
                y = False
                s1.push(x,y)            
    if s1.getsize() > 0:
        return True
    else:
        return False
                
            
#### Implement Your Code Here
    

string = input()
ans = checkRedundant(string)
if ans is True:
    print('true')
else:
    print('false')




