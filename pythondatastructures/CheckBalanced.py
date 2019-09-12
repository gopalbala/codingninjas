
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Stack:
    ### Implement all these functions here
    
    def __init__(self):
        self.__head = None
        self.__size = 0

    def push(self,data):
        if self.__head is None:
            self.__head = Node(data)
        else:
            node = Node(data)
            node.next = self.__head
            self.__head = node
        self.__size = self.__size + 1
        
    def pop(self):
        if self.__head is None:
            return None
        else:
            node = self.__head
            self.__head = self.__head.next
            self.__size = self.__size - 1
            return node.data
    # Return 0 if stack is empty. Don't display any other message
    def top(self):
        if self.__head is None:
            return 0
        else:
            return self.__head.data
    # Return 0 if stack is empty. Don't display any other message
    def isEmpty(self):
        if self.__head is None:
            return 0
        
    def getSize(self):
        return self.__size
    
def checkBalanced(expr):
    st = Stack()
    for s in expr.split():
        if s == "(" or s == "{" or s == "[":
            st.push(s)
        elif s == ")":
            print(st.top())
            if st.top() != "(":
                return False
            st.pop()
        elif s == "}":
            print(st.top())
            if st.top() != "{":
                return False
            st.pop()
        elif s == "]":
            print(st.top())
            if st.top() != "[":
                return False
            st.pop()
        else:
            pass
    return True
        
            
### Implement your code here

exp=input()
if checkBalanced(exp):
    print('true')
else:
    print('false')

