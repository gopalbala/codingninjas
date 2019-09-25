import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return None
    
    q = queue.Queue()
    q.put(root)
    q.put(None)
    print(root.data)
    while not q.empty():
        t = q.get()
        if t is None and not q.empty():
            print()
            q.put(None)
            continue
        if t is not None and t.left != None and t.left.data != -1:
            q.put(t.left)
            print(t.left.data, end=' ')
        if t is not None and t.right != None and t.right.data != -1:
            q.put(t.right)
            print(t.right.data,end=' ')
        

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
#n=int(input())
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
printLevelATNewLine(root)
