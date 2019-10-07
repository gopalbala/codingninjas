import queue
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def containsX(tree, x):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if tree is None:
        return 0
    q = queue.Queue()
    q.put(tree)
    while not q.empty():
        t = q.get()
        if t.data == x:
            return True
        if t is None and q.qsize() == 0:
            break
        for tn in t.children:
                q.put(tn)
    return False
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
x=int(input())
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
if containsX(tree,x):
    print('true')
else:
    print('false')
