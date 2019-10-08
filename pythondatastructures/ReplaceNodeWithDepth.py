import queue
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def replacewithDepth(tree):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    q = queue.deque()
    tree.data = 0
    q.append(tree)
    height = 1
    q.append(None)
    curr = tree
    while len(q) > 0:
        t = q.popleft()
        if t is None and len(q) == 0:
            break
        if t is None:
            q.append(None)
            height = height + 1
        else:
            t.data = height -1
            for tn in t.children:
                q.append(tn)

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

def printLevelAtNewLine(tree):
    q = [tree]
    newq = []
    while q:
        parent = q.pop(0)
        print(parent.data, end=' ')
        for child in parent.children:
            newq.append(child)
        if len(q)==0:
            q = newq
            newq = []
            print()  # Move to next Line

# Main
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
replacewithDepth(tree)
printLevelAtNewLine(tree)
