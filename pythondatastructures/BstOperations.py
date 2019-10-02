class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None
        self.numNodes = 0

    def printTreeHelper(self, root):
        if root == None:
            return
        print(root.data, end=":")
        if root.left != None:
            print("L:", end='')
            print(root.left.data, end=',')
        if root.right != None:
            print("R:", end='')
            print(root.right.data, end='')
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)

    def printTree(self):
        self.printTreeHelper(self.root)

    def search(self, data):
        root = search(self.root, data)
        if root is None:
            return False
        else:
            return True
    # Implement this function here

    def minElement(root):
        if root.left is None:
            return root
        return minElement(root.left)

    def insert(self, data):
        if self.root is None:
            self.root = BinaryTreeNode(data)
        else:
            insert(self.root, data)
    # Implement this function here
    def delete(self, data):
        deleted, newRoot = deleteHelper(self.root, data)
        if deleted:
            self.numNodes -= 1
            self.root = newRoot
            return deleted
        # delete(self.root, data)

def deleteHelper(root, data):
    if root is None:
        return False, None
    if root.data < data:
        deleted, newRight = deleteHelper(root.right, data)
        root.right = newRight
        return deleted, root
    if root.data > data:
        deleted, newLeft = deleteHelper(root.left, data)
        root.left = newLeft
        return deleted, root
    if root.left is None and root.right is None:
        return True, None
    if root.left is None:
        return True, root.right
    if root.right is None:
        return True, root.left
    newRoot = minElement(root.right)
    root.data = newRoot.data
    deleted, newRightNode = deleteHelper(root.right,newRoot.data)
    root.right = newRightNode
    return True, root
    
def delete(root, data):
    # delete(self.root, data)
    if root.data == data:
        # found the node we need to delete
        if root.right and root.left: 

        # get the successor node and its parent 
            [psucc, succ] = _findMin(root.right, root)

        # splice out the successor
        # (we need the parent to do this) 

            if psucc.left == succ:
                psucc.left = succ.right
            else:
                psucc.right = succ.right

        # reset the left and right children of the successor

            succ.left = root.left
            succ.right = root.right

            return succ                

        else:
            # "easier" case
            if root.left:
                return root.left    # promote the left subtree
            else:
                return root.right   # promote the right subtree 
    else:
        if root.data > data:          # key should be in the left subtree
            if root.left:
                root.left = delete(root.left,data)
            # else the key is not in the tree 

        else:                       # key should be in the right subtree
            if root.right:
                root.right = delete(root.right,data)

    return root

def _findMin(root, parent):
    """ return the minimum node in the current tree and its parent """

    # we use an ugly trick: the parent node is passed in as an argument
    # so that eventually when the leftmost child is reached, the 
    # call can return both the parent to the successor and the successor

    if root.left:
        return _findMin(root.left, root)
    else:
        return [parent, root]
# Implement this function here

def count(self):
    return self.numNodes


def search(root, data):
    if root is None:
        return None
    if root.data == data:
        return root
    if data < root.data:
        return search(root.left, data)
    else:
        return search(root.right, data)

def minElement(root):
        if root.left is None:
            return root
        return minElement(root.left)
          
def insert(root, data):
    if root is None:
        root = BinaryTreeNode(data)
        return
    if root.left is not None and data < root.data:
        insert(root.left, data)
    elif root.left is None and data < root.data:
        root.left = BinaryTreeNode(data)
    if root.right is not None and data > root.data:
        insert(root.right, data)
    elif root.right is None and data > root.data:
        root.right = BinaryTreeNode(data) 
    
b = BST()
li = [int(ele) for ele in input().split()]
i = 0
while(i < (len(li) )):
    choice = li[i]
    if choice == 1:
        data = li[i+1]
        b.insert(data)
        i+=2
    elif choice == 2:
        data = li[i+1]
        b.delete(data)
        i+=2
    elif choice == 3:
        data = li[i+1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
        i+=2
    else:
        b.printTree()
        i+=1
        
    
