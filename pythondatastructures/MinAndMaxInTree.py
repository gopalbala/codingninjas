#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


INT_MIN = -2147483648
INT_MAX = 2147483647
# Problem ID 1567, Find the minimum and maximum value

class Output:
    def __init__(self,min,max):
        self.min = min
        self.max = max

def minMax(root, output):
    # Given a binary tree, find and return the min and max data value of given
    # binary tree. Return maximum and minimum from this function only. Largest
    # and smallest data possible is provided through INT_MAX and INT_MIN
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return (output.min, output.max)
    minMax(root.left, output)
    minMax(root.right, output)
    if root.data != -1 and root.data < output.min:
        output.min = root.data
    if root.data != -1 and root.data > output.max:
        output.max = root.data
    return (output.min, output.max)

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
minimum, maximum = minMax(root, Output(INT_MAX, INT_MIN))
print(maximum, minimum)
