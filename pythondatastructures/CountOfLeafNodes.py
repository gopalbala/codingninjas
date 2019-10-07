import queue
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def leafNodeCount(tree):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if tree is None:
        return 0
    leafCount = 0
    q = queue.Queue()
    q.put(tree)
    while not q.empty():
        t = q.get()
        if len(t.children) == 0:
            leafCount+=1
        for tn in t.children:
            q.put(tn)
    return leafCount

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
print(leafNodeCount(tree))
