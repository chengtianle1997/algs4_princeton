# queue for level order iterate
from queue import Queue
# visualize
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.left = None
        self.right = None
        self.count = 1
        
class BST:
    def __init__(self):
        self.root = None
        self.node_list = []
        # Visualize Param
        self.step = 15
        self.R = self.step * 0.6
        self.start_space = 1

    def size(self, x=0):
        if x == 0:
            return self.size(self.root)
        if x == None:
            return 0
        return x.count

    # Get the value of a key
    def get(self, key):
        x = self.root
        while not x == None:
            cmp = self.compare(key, x.key)
            if cmp < 0:
                x = x.left
            elif cmp > 0:
                x = x.right
            elif cmp == 0:
                return x.val
        return None
    
    # Insert a pair of key and value
    def put(self, key, val):
        self.root = self.put_p(self.root, key, val)

    def put_p(self, x, key, val):
        if x == None:
            return Node(key, val)
        cmp = self.compare(key, x.key)
        if cmp < 0:
            x.left = self.put_p(x.left, key, val)
        elif cmp > 0:
            x.right = self.put_p(x.right, key, val)
        elif cmp == 0:
            x.val = val
        x.count = 1 + self.size(x.left) + self.size(x.right)
        return x

    # Return the min key
    def min(self):
        x = self.root
        while not x == None:
            if x.left == None:
                return x.key
            x = x.left
        return None

    # Return the max key
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
        cmp = self.compare(K, x.key)
        # Case 1: K == x.key
        if cmp == 0:
            return x
        # Case 2: K < x.key
        # x.key is still too big, try go left to find a smaller one
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

    # Ceil: Find the Min key >= K
    def ceil(self, K):
        x = self.ceil_p(self.root, K)
        if x == None:
            return None
        return x.key

    def ceil_p(self, x, K):
        if x == None:
            return None
        cmp = self.compare(K, x.key)
        # Case 1: K == x.key
        if cmp == 0:
            return x
        # Case 2: K > x.key
        # x.key is still smaller than K, try go right to find a bigger one
        if cmp > 0:
            return self.ceil_p(x.right, K)
        # Case 3: K < x.key
        # x.key is already bigger than K, try go left to find a smaller one
        # that is still bigger but closer to K
        if cmp < 0:
            t = self.ceil_p(x.left, K)
            # if found
            if not t == None:
                return t
            # if not found
            else:
                return x

    # Print the Binary Search Tree in ascending sequence
    def printTreeSeq(self):
        self.node_list = []
        self.printTreeSeq_p(self.root)
        return self.node_list
    
    def printTreeSeq_p(self, root):
        if root == None:
            return
        self.printTreeSeq_p(root.left)
        # print(root.key)
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

    # Hibbard Deletion: Delete a Node with key K
    def delete(self, K):
        self.root = self.delete_p(self.root, K)
    
    def delete_p(self, x, K):
        if x == None:
            return None
        cmp = self.compare(K, x.key)
        # Search for the key
        if cmp < 0:
            x.left = self.delete_p(x.left, K)
        elif cmp > 0:
            x.right = self.delete_p(x.right, K)
        else:
            # Node with single child or no child: replace the node with its child
            if x.right == None:
                return x.left
            if x.left == None:
                return x.right
            # Node with two child: replace the node with the min of its right subtree
            # Save the node
            t = x
            # Find the min of the right sub-tree
            x = self.min(x.right)
            # Delete the min of the right sub-tree
            x.right = self.deleteMin(t.right)
            x.left = t.left
        x.count = 1 + self.size(x.left) + self.size(x.right)
        return x

    def compare(self, keyA, keyB):
        if keyA > keyB:
            return 1
        if keyA < keyB:
            return -1
        if keyA == keyB:
            return 0
        return None

    def level_order(self):
        level_list = []
        q = Queue(maxsize=0)
        if self.root == None:
            return level_list
        q.put(self.root)
        while not q.empty():
            t = q.get()
            level_list.append(t.key)
            if t.left:
                q.put(t.left)
            if t.right:
                q.put(t.right)
        return level_list

    def height(self):
        height_count = 0
        q = Queue(maxsize=0)
        if self.root == None:
            return None
        q.put(self.root)
        while not q.empty():
            q_l = Queue(maxsize=0)
            while not q.empty():
                q_l.put(q.get())
            while not q_l.empty():
                t = q_l.get()
                if t.left:
                    q.put(t.left)
                if t.right:
                    q.put(t.right)
            # print("\n", end="")
            height_count += 1
        return height_count
    
    def level_order_byline(self):
        level_list = []
        q = Queue(maxsize=0)
        if self.root == None:
            return None
        q.put(self.root)
        while not q.empty():
            level_list_line = []
            q_l = Queue(maxsize=0)
            while not q.empty():
                q_l.put(q.get())
            while not q_l.empty():
                t = q_l.get()
                if t.key:
                    # print(t.key, end=" ")
                    level_list_line.append(t.key)
                if t.left:
                    q.put(t.left)
                if t.right:
                    q.put(t.right)
            # print("\n", end="")
            level_list.append(level_list_line)
        return level_list
    
    def visualize(self):
        n = self.height()
        # visualize param
        line_count = 1
        q = Queue(maxsize=0)
        if n == None:
            print("Error: Try to visualize a empty tree!")
            return
        fig = plt.figure()
        ax = fig.add_subplot(111)
        q = Queue(maxsize=0)
        q_pos = Queue(maxsize=0)
        if self.root == None:
            return
        q.put(self.root)
        top_space = (n - 2 + 2 ** (n - 1)) * self.step
        root_pos = [top_space, top_space]
        q_pos.put(root_pos)
        # Draw Root Node
        self.drawNode(ax, self.root.key, root_pos)
        while not q.empty():
            q_l = Queue(maxsize=0)
            while not q.empty():
                q_l.put(q.get())
            while not q_l.empty():
                t = q_l.get()
                pos = q_pos.get()
                if t.left:
                    l_pos = self.drawLeftChild(ax, t.left.key, line_count, n, pos)
                    q_pos.put(l_pos)
                    q.put(t.left)
                if t.right:
                    r_pos = self.drawRightChild(ax, t.right.key, line_count, n, pos)
                    q_pos.put(r_pos)
                    q.put(t.right)
            line_count += 1
        plt.axis('equal')
        plt.axis('off')
        plt.show()

    def drawNode(self, ax, key, pos):
        circle = mpatches.Circle(pos, radius=self.R)
        ax.add_patch(circle)
        ax.text(pos[0], pos[1], str(key), size=self.R*2.5, horizontalalignment='center', verticalalignment='center')

    def drawLine(self, ax, pos_start, pos_stop):
        out_range = 1.1
        dist = ((pos_start[0] - pos_stop[0]) ** 2 + (pos_start[1] - pos_stop[1]) ** 2) ** 0.5
        xr = ((pos_start[0] - pos_stop[0]) * self.R / dist) * out_range
        yr = ((pos_start[1] - pos_stop[1]) * self.R / dist) * out_range
        line_x = [pos_start[0] - xr, pos_stop[0] + xr]
        line_y = [pos_start[1] - yr, pos_stop[1] + yr]
        ax.plot(line_x, line_y, '-', color='grey', linewidth=self.step * 0.4)

    def drawLeftChild(self, ax, key, line, n, pos_parent):
        space_child = (2 * (n - line) - 1) * self.step * (1 + line / (1.5 * n))
        left_child_pos = [pos_parent[0] - space_child * 0.6, pos_parent[1] - space_child]
        self.drawNode(ax, key, left_child_pos)
        self.drawLine(ax, pos_parent, left_child_pos)
        return left_child_pos

    def drawRightChild(self, ax, key, line, n, pos_parent):
        space_child = (2 * (n - line) - 1) * self.step * (1 + line / (1.5 * n))
        right_child_pos = [pos_parent[0] + space_child * 0.6, pos_parent[1] - space_child]
        self.drawNode(ax, key, right_child_pos)
        self.drawLine(ax, pos_parent, right_child_pos)
        return right_child_pos

# Test Node
# key = ['S', 'E', 'A', 'R', 'C', 'H', 'T', 'R', 'E', 'E', 'B', 'I', 'N', 'A', 'R', 'Y']
# val = [ 1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13,  14,  15,  16]
# key = ['S', 'E', 'A', 'R', 'C']
# val = [ 1,   2,   3,   4,   5]
key = ['S', 'E', 'A', 'R', 'C', 'H', 'T', 'R', 'E', 'E']
val = [ 1,   2,   3,   4,   5,   6,   7,   8,   9,   10]
bst = BST()
root = None
# put
for i in range(len(key)):
    root = bst.put(key[i], val[i])
# get size
print("Size of Tree: {}".format(bst.size()))
# get
for i in range(len(key)):
    print("key:{}, value:{}".format(key[i], bst.get(key[i])))
# min & max
print("Min:{}, Max:{}".format(bst.min(), bst.max()))
# floor & ceiling
test_floor = 'B'
print("Floor({}) = {}".format(test_floor, bst.floor(test_floor)))
test_ceil = 'D'
print("Ceil({}) = {}".format(test_ceil, bst.ceil(test_ceil)))
# delete min
print("Delete Min:")
print("->Before: size = {}".format(bst.size()), end=" ")
print(bst.printTreeSeq())
bst.deleteMin()
print("->After: size = {}".format(bst.size()), end=" ")
print(bst.printTreeSeq())
# delete max
print("Delete Max:")
print("->Before: size = {}".format(bst.size()), end=" ")
print(bst.printTreeSeq())
bst.deleteMax()
print("->After: size = {}".format(bst.size()), end=" ")
print(bst.printTreeSeq())
# Hibbard deletion: Delete a node with key K
K = 'H'
print("Hibbard Deletion: Delete {}".format(K))
print("->Before: size = {}".format(bst.size()), end=" ")
print(bst.printTreeSeq())
bst.delete(K)
print("->After: size = {}".format(bst.size()), end=" ")
print(bst.printTreeSeq())

# Re-input All items in BST
bst = BST()
for i in range(len(key)):
    root = bst.put(key[i], val[i])
# Level order print
print("level order:")
print(bst.level_order())
print("level order by line:")
print(bst.level_order_byline())
# BST visualization
bst.visualize()




