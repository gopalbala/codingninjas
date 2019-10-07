import sys
import queue
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)
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
def heightOfTree(tree):
    if tree is None:
        return 0
    height = 1
    q = queue.Queue()
    q.put(tree)
    q.put(None)
    while not q.empty():
        t = q.get()
        if t is None and q.qsize() == 0:
            break
        if t is None:
            q.put(None)
            height+=1
        else:
            for tn in t.children:
                q.put(tn)
    return height

# Main
mx = -sys.maxsize - 1
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(heightOfTree(tree))