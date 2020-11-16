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
    
    # Find the Min key <= K
    def ceil(self, K):
        x = self.ceil_p(self.root, K)
        if x == None:
            return None
        return x.key
    
    def ceil_p(self, x, K):
        if x == None:
            return None
            

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
        
