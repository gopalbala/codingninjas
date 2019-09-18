import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLevelWise(root):
    # Given a binary tree, print the tree in level wise order. For printing
    # a node with data N, you need to follow the exact format: 
    # N:L:x,R:y
    # wherer, N is data of any node present in the binary tree. x and y are the
    # values of left and right child of node N. Print -1. if any child is null.
    # There is no space in between. You need to print all nodes in the level
    # order form in different lines.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return
    q = queue.Queue()
    q.put(root)
    q.put(None)
    while not q.empty():
        n = q.get()
        if n is None and not q.empty():
            print()
            q.put(None)
            continue
        if n is not None:
            print(str(n.data)+":",end='' )
        if n is not None and n.left is not None:
            q.put(n.left)
            print("L:"+str(n.left.data), end = '')
        if n is not None and n.right is not None:
            q.put(n.right)
            print("R:"+str(n.right.data), end = '')
            
    

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
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
printLevelWise(root)
