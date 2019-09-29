import queue
import math
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBST(lst):
    # Given a sorted integer array A of size n which contains all unique
    # elements. You need to construct a balanced BST from this input array.
    # Return the root of constructed BST. If array size is even, take first mid
    # as root.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if not lst: 
        return None
    mid = len(lst)//2 + len(lst) % 2 -1
    # print(mid)
    root = BinaryTreeNode(lst[mid]) 
    root.left = constructBST(lst[:mid])
    root.right = constructBST(lst[mid+1:])
    return root

def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root,k1,k2):
    if root is None:
        return None
    inOrder(root.left,k1,k2)
    if root.data >= k1 and root.data <= k2:
        print(root.data, end = ' ')
    inOrder(root.right,k1,k2)
    # Main
n=int(input())
lst=[int(i) for i in input().strip().split()]
root=constructBST(lst)
preOrder(root)
