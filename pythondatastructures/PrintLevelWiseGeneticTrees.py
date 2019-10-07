import queue
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def printLevelWiseTree(tree):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if tree is None:
        return
    q = queue.Queue()
    q.put(tree)
    q.put(None)
    while not q.empty():
        t = q.get()
        if t is not None:
            print(str(t.data)+":", end = '')
        if t is None and q.qsize() == 0:
            break
        if t is None:
            q.put(None)
        else:
            s = len(t.children)
            for i in range(s):
                if i < s-1:
                    q.put(t.children[i])
                    print(str(t.children[i].data)+",", end = '')
                else:
                    q.put(t.children[i])
                    print(str(t.children[i].data), end = '')
            print()
            
        
                 
def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
printLevelWiseTree(tree)
