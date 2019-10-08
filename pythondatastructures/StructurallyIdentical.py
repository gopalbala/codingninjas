import queue
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def isIdentical(tree1, tree2):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if tree1 is None and tree2 is None:
        return True
    if (tree1 is None and tree2 is not None) or (tree1 is not None and tree2 is None):
        return False
    t1 = []
    t2 = []
    q = queue.Queue()
    q.put(tree1)
    ident = True
    t1.append(tree1.data)
    while not q.empty():
        t = q.get()
        for tn in t.children:
            q.put(tn)
            t1.append(tn.data)
    q = queue.Queue()
    q.put(tree2)
    ident = True
    t2.append(tree2.data)
    while not q.empty():
        t = q.get()
        for tn in t.children:
            q.put(tn)
            t2.append(tn.data)
    if len(t1) != len(t2):
        return False
    for i in range(len(t1)):
        if t1[i] != t2[i]:
            return False
    return True

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
arr1 = list(int(x) for x in input().strip().split(' '))
tree1 = createLevelWiseTree(arr1)
arr2 = list(int(x) for x in input().strip().split(' '))
tree2 = createLevelWiseTree(arr2)
if isIdentical(tree1, tree2):
    print('true')
else:
    print('false')
