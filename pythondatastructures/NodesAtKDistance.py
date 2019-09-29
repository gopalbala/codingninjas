import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printNodesAtK(root, node, k):
    if root is None:
        return
    lst, match = findNodePath(root, node, [])
    depth = k
    for i in range(len(lst)-1, -1, -1):
        (curr, lrflg) = lst[i]
        if lrflg == '' or depth == 0:
            printNodesAtDepth(curr, depth)
        else:
            if lrflg == 'L':
                printNodesAtDepth(curr.right, depth-1)
            else:
                printNodesAtDepth(curr.left, depth - 1)
        depth -= 1


def printNodesAtDepth(root, depth, level=0):
    if root is None or level > depth:
        return
    if level == depth:
        print(root.data)
        return
    printNodesAtDepth(root.left, depth, level+1)
    printNodesAtDepth(root.right, depth, level+1)

    return


def findNodePath(root, node, lst):
    if root is None:
        return lst, False
    if root.data == node:
        lst.append((root, ''))
        return lst, True
    if root.left is not None and root.left.data == node:
        lst.append((root, 'L'))
        lst.append((root.left, ''))
        return lst, True
    if root.right is not None and root.right.data == node:
        lst.append((root, 'R'))
        lst.append((root.right, ''))
        return lst, True
    lst.append((root, 'L'))
    lst, match = findNodePath(root.left, node, lst)
    if not match:
        lst.pop()
        lst.append((root, 'R')) 
        lst, match = findNodePath(root.right, node, lst)
        if not match:
            lst.pop()
    
    return lst, match


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
n = int(input())
k = int(input())
printNodesAtK(root, n, k)
