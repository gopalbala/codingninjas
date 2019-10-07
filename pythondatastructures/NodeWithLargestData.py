import sys
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def maxDataNode(tree):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    global mx
    if tree is None:
        return mx
    for tn in tree.children:
        if tn.data > mx:
            mx = tn.data
        maxDataNode(tn)
    return mx
    

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
mx = -sys.maxsize - 1
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
mx = tree.data
print(maxDataNode(tree))
