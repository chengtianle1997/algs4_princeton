# queue for level order iterate
from queue import Queue
# visualize
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BLACK = False
RED = True

class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.left = None
        self.right = None
        self.color = BLACK
        self.count = 1

def isRed(node):
    if node == None:
        return False
    return node.color == RED

def compare(KeyA, KeyB):
    if KeyA > KeyB:
        return 1
    elif KeyA < KeyB:
        return -1
    else:
        return 0

class LLRBTree:
    def __init__(self):
        self.root = None
        self.node_list = []

    def size(self, x=0):
        if x == 0:
            return self.size(self.root)
        if x == None:
            return 0
        return x.count
        
    def rotateLeft(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RED
        return x
    
    def rotateRight(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RED
        return x
    
    def flipColors(self, h):
        # just change the color
        h.color = RED
        h.left.color = BLACK
        h.right.color = BLACK

    def get(self, key):
        x = self.root
        while not x == None:
            cmp = compare(key, x.key)
            if cmp > 0:
                x = x.right
            elif cmp < 0:
                x = x.left
            elif cmp == 0:
                # find the key
                return x.val
        # cannot find the key
        return None
    
    def put(self, key, val):
        self.root = self.put_p(self.root, key, val)

    def put_p(self, x, key, val):
        if x == None:
            return Node(key, val)
        cmp = compare(key, x.key)
        if cmp < 0:
            x.left = self.put_p(x.left, key, val)
        elif cmp > 0:
            x.right = self.put_p(x.right, key, val)
        elif cmp == 0:
            # update the value
            x.val = val
        
        x.count = 1 + self.size(x.left) + self.size(x.right)
        
        # Red-Black Operations
        if isRed(x.right) and not isRed(x.left):
            # Lean Right -> Lean Left
            h = self.rotateLeft(x)
        if isRed(x.left) and isRed(x.left.left):
            # Balance 4-node
            x = self.rotateRight(x)
        if isRed(x.left) and isRed(x.right):
            # Split 4-node
            self.flipColors(x)
        
        return x

    # Find the min key
    def min(self):
        x = self.root
        while not x == None:
            if x.left == None:
                return x.key
            x = x.left
        return None
    
    # Find the max key
    def max(self):
        x = self.root
        while not x == None:
            if x.right == None:
                return x.key
            x = x.right
        return None

    # Floor: Find the max key <= K
    def floor(self, K):
        x = self.floor_p(self.root, K)
        if x == None:
            return None
        return x.key
    
    def floor_p(self, x, K):
        if x == None:
            return None
        cmp = compare(K, x.key)
        # Case 1: K == x.key
        if cmp == 0:
            return x
        # Case 2: K < x.key
        # x.key is still too big , try go left to find a smaller one
        elif cmp < 0:
            return self.floor_p(x.left, K)
        # Case 3: K > x.key
        # x.key is already smaller than K, try to find a bigger one
        # that is still smaller but more closer to K
        elif cmp > 0:
            # Try to find a bigger one
            t = self.floor_p(x.right, K)
            # if found
            if not t == None:
                return t
            # if not found
            else:
                return x
    
    # Find the Min key >= K
    def ceil(self, K):
        x = self.ceil_p(self.root, K)
        if x == None:
            return None
        return x.key
    
    def ceil_p(self, x, K):
        if x == None:
            return None
        cmp = compare(K, x.key)
        # Case 1: K == x.key
        if cmp == 0:
            return x
        # Case 2: K > x.key
        # x.key is still too small, try to find a bigger one
        elif cmp > 0:
            return self.ceil_p(x.right, K)
        # Case 3: K < x.key
        # x.key is already bigger than K, try to find a smaller one
        # that is still smaller but more closer to K
        elif cmp < 0:
            # Try to find a smaller one
            t = self.ceil_p(x.left, K)
            # if found
            if not t == None:
                return t
            # if not found
            else:
                return x

    # Print the Red Black Tree in ascending sequence
    def printTreeSeq(self):
        self.node_list = []
        self.printTreeSeq_p(self.root)
        return self.node_list

    def printTreeSeq_p(self, root):
        if root == None:
            return
        self.printTreeSeq_p(root.left)
        self.node_list.append(root.key)
        self.printTreeSeq_p(root.right)
    
    # Delete MinNode
    def deleteMin(self):
        if self.root == None:
            return
        self.root = self.deleteMin_p(self.root)
    
    # Go left until finding a node with no left node
    # Replace that node with its right link
    # Update subtree counts
    def deleteMin_p(self, x):
        if x.left == None:
            return x.right
        x.left = self.deleteMin_p(x.left)
        x.count = 1 + self.size(x.left) + self.size(x.right)
        return x
    
    # Delete MaxNode
    def deleteMax(self):
        if self.root == None:
            return
        self.root = self.deleteMax_p(self.root)
    
    # Go right until finding a node with no right node
    # Replace that node with its left link
    # Update subtree counts
    def deleteMax_p(self, x):
        if x.right == None:
            return x.left
        x.right = self.deleteMax_p(x.right)
        x.count = 1 + self.size(x.left) + self.size(x.right)
        return x
    

# Test Demo
key = ['S', 'E', 'A', 'R', 'C', 'H', 'T', 'R', 'E', 'E']
val = [ 1,   2,   3,   4,   5,   6,   7,   8,   9,   10]
llrb = LLRBTree()
root = None
# put
for i in range(len(key)):
    llrb.put(key[i], val[i])
# get
for i in range(len(key)):
    print("key:{}, value:{}".format(key[i], llrb.get(key[i])))
# min & max
print("Min:{}, Max:{}".format(llrb.min(), llrb.max()))
# floor & ceiling
test_floor = 'B'
print("Floor({}) = {}".format(test_floor, llrb.floor(test_floor)))
test_ceil = 'D'
print("Ceil({}) = {}".format(test_ceil, llrb.ceil(test_ceil)))
# delete min
print("Delete Min:")
print("->Before: size = {}".format(llrb.size()), end=" ")
print(llrb.printTreeSeq())
llrb.deleteMin()
print("->After: size = {}".format(llrb.size()), end=" ")
print(llrb.printTreeSeq())
# delete max
print("Delete Max:")
print("->Before: size = {}".format(llrb.size()), end=" ")
print(llrb.printTreeSeq())
llrb.deleteMax()
print("->After: size = {}".format(llrb.size()), end=" ")
print(llrb.printTreeSeq())
