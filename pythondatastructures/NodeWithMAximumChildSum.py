import queue
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def maxSumNode(tree):
    # Return the node and its sum
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if tree is None:
        return None
    q = queue.Queue()
    q.put(tree)
    nMx = tree
    sm = 0
    while not q.empty():
        t = q.get()
        if t is not None:
            if t.children is not None:
                s = 0
                for tn in t.children:
                    q.put(tn)
                    s+= tn.data
                # s = sum(t.children)
                if s > sm:
                    nMx = t
                    sm = s
    return (nMx,sm)

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
temp, tempSum = maxSumNode(tree)
print(temp.data)
