import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTreePostOrder(postorder, inorder):
    # Given Postorder and Inorder traversal of a binary tree, create the binary
    # tree associated with the traversals.You just need to construct the tree
    # and return the root. For 8 Nodes with following input:
    # postOrder: 8 4 5 2 6 7 3 1
    # inOrder: 4 8 2 5 1 6 3 7
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    # if len(postorder) == 0:
    #     return None
    # elem = postorder[len(postorder)-1]
    # n = BinaryTreeNode(elem)
    # iIndex = -1
    # for i in range(len(inorder)):
    #     if inorder[i] == elem:
    #         iIndex = i
    #         break
    # leftInorder = inorder[0:iIndex]
    # rightInorder = inorder[iIndex+1:]

    # print(*rightInorder)
    # print(*leftInorder)

    # lenOfLeft = len(leftInorder)

    # rightPostOrder = postOrder[0:lenOfLeft]
    # leftPostOrder = postOrder[lenOfLeft+1:len(postOrder)-1]

    # if len(leftInorder) > 0 and len(rightInorder) > 0:
    #     elem.left = buildTreePostOrder(postorder, leftInorder)
    #     elem.right = buildTreePostOrder(postorder, rightInorder)
    # return elem
    pIndex = [len(inorder) - 1]
    return buildUtil(inorder, postorder, 0, len(inorder)-1, pIndex)

def buildUtil(In, post, inStrt, inEnd, pIndex): 
      
    # Base case  
    if (inStrt > inEnd):  
        return None
  
    # Pick current node from Postorder traversal  
    # using postIndex and decrement postIndex  
    node = BinaryTreeNode(post[pIndex[0]])  
    pIndex[0] -= 1
  
    # If this node has no children  
    # then return  
    if (inStrt == inEnd):  
        return node  
  
    # Else find the index of this node  
    # in Inorder traversal  
    iIndex = search(In, inStrt, inEnd, node.data)  
  
    # Using index in Inorder traversal,  
    # construct left and right subtress  
    node.right = buildUtil(In, post, iIndex + 1,  
                                  inEnd, pIndex)  
    node.left = buildUtil(In, post, inStrt,  
                        iIndex - 1, pIndex)  
  
    return node 

def search(arr, strt, end, value): 
    i = 0
    for i in range(strt, end + 1): 
        if (arr[i] == value):  
            break
    return i 

def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
    if root == None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left != None:
                outputQ.put(curr.left)
            if curr.right != None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ


# Main
n = int(input())
postOrder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreePostOrder(postOrder, inorder)
printLevelATNewLine(root)
