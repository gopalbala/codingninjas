# Read input as specified in the question.
# Print output as specified in the question.
import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def kdistance(root, n, k):
    level = 0
    if root is None:
        return
    q = queue.Queue()
    q.put(root)
    q.put(None)
    found = False
    while not q.empty():
        node = q.get()
        if node is None:
            if found:
                level += 1
                print()
            continue
        if node.data == n:
            found = True
            level+=1
        if level == k and node.data != -1 and node.data != n:
            print(node.data, end = ' ')
        if node.left is not None and node.left.data != -1:
            q.put(node.left)
            # if level == k:
            #     print(node.data, end = ' ')
        if node.right is not None and node.right.data != -1:
            q.put(node.right)
            # if level == k:
            #     print(node.data, end = ' ')
        
def printkDistanceNodeDown(root, k): 
      
    # Base Case 
    if root is None or k< 0 : 
        return 
      
    # If we reach a k distant node, print it 
    if k == 0 : 
        print(root.data )
        return 
    # Recur for left and right subtee 
    printkDistanceNodeDown(root.left, k-1) 
    printkDistanceNodeDown(root.right, k-1) 

def printkDistanceNode(root, target, k): 
      
    # Base Case 1 : IF tree is empty return -1 
    if root is None: 
        return -1
  
    # If target is same as root. Use the downward function 
    # to print all nodes at distance k in subtree rooted with 
    # target or root 
    if root == target: 
        printkDistanceNodeDown(root, k) 
        return 0 
      
    # Recur for left subtree 
    dl = printkDistanceNode(root.left, target, k) 
      
    # Check if target node was found in left subtree 
    if dl != -1: 
          
        # If root is at distance k from target, print root 
        # Note: dl is distance of root's left child  
        # from target 
        if dl +1 == k : 
            print(root.data)
      
        # Else go to right subtreee and print all k-dl-2 
        # distant nodes  
        # Note: that the right child is 2 edges away from 
        # left chlid 
        else: 
            printkDistanceNodeDown(root.right, k-dl-2) 
  
        # Add 1 to the distance and return value for 
        # for parent calls  
        return 1 + dl 
  
    # MIRROR OF ABOVE CODE FOR RIGHT SUBTREE 
    # Note that we reach here only when node was not found 
    # in left subtree 
    dr = printkDistanceNode(root.right, target, k) 
    if dr != -1: 
        if (dr+1 == k): 
            print(root.data )
        else: 
            printkDistanceNodeDown(root.left, k-dr-2) 
        return 1 + dr 
  
    # If target was neither present in left nor in right subtree 
    return -1

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
printkDistanceNode(root,n,k)