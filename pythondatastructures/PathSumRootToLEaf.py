import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def rootToLeafPathsSumToK(root, k, lst):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return
    if root.data != -1:
        lst.append(root.data)
    rootToLeafPathsSumToK(root.left, k, lst)
    rootToLeafPathsSumToK(root.right, k, lst)
    sum = 0
    if (root.left is None ) and (root.right is None):
        for i in lst:
            sum += i
        if sum == k:
            print(*lst)
    lst.pop(-1)

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
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
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root


# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
k = int(input())
rootToLeafPathsSumToK(root, k, [])
