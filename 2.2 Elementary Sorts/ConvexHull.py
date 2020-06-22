from random import uniform
import matplotlib.pyplot as plt
import math

# Stack Class
class Stack(object):
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peak(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)

    def getitems(self):
        return self.items

# Generate Random Points
def GenerateRandPoint(n, xmin, xmax, ymin, ymax):
    pointx, pointy = [], []
    pointx = [uniform(xmin, xmax) for x in range(n)]
    pointy = [uniform(ymin, ymax) for x in range(n)]
    return pointx, pointy

# Display points with matplotlib
def DisplayPoint(pointx, pointy):
    plt.scatter(pointx, pointy, 4)
    plt.show()

point_x, point_y = GenerateRandPoint(100, 0, 10, 0, 10)
DisplayPoint(point_x, point_y)

# Find the minimum y for start point
# This step guarantees that other points all displayed on the upper plane
# We can use arccos to calculate and do not need to worry about the same cosine value
def FindStartPoint(pointy):
    min_i, min_v = 0, point_y[0]
    for i in range(1, len(point_y)):
        if point_y[i] < min_v:
            min_i = i
            min_v = point_y[i]
    return min_i

# CCW
def CCW(ax, ay, bx, by, cx, cy):
    if (((bx-ax)*(cy-ay) - (by-ay)*(cx-ax)) > 0):
        return True
    else:
        return False

# Sort other points by polar angle, take Selection Sort for example
def SortPoint(start_pt, point_x, point_y):
    # Calculate the Polar Angle
    n = len(point_x)
    polar_angle = []
    # Exchange Start Point and Point 0
    point_x[0], point_x[start_pt] = point_x[start_pt], point_x[0]
    point_y[0], point_y[start_pt] = point_y[start_pt], point_y[0]
    polar_angle.append(0)
    # Calculate Point 1 to Point n-1
    for i in range(1, n):
        long_side = math.sqrt((point_y[i] - point_y[0])**2 + (point_x[i] - point_x[0])**2)
        if(long_side == 0):
            polar_angle.append(math.pi)
        else:
            cos_value = (point_x[i] - point_x[0]) / long_side
            polar_angle.append(math.acos(cos_value))

    # Attention: Point 0 is Start Point, Sort Point 1 to Point n-1 only
    for i in range(1, n):
        min, min_index = polar_angle[i], i
        for j in range(i+1, n):
            if (polar_angle[j] < min):
                min = polar_angle[j]
                min_index = j
        polar_angle[min_index], polar_angle[i] = polar_angle[i], polar_angle[min_index]
        point_x[min_index], point_x[i] = point_x[i], point_x[min_index]
        point_y[min_index], point_y[i] = point_y[i], point_y[min_index]
    point_x.append(point_x[0])
    point_y.append(point_y[0])
    return point_x, point_y
           
# Convex Hull
def ConvexHull(point_x, point_y):
    n, m = len(point_x), len(point_y)
    if (n != m):
        print("Input Error: Different length of x and y")
        return -1
    start_pt = FindStartPoint(point_y)
    point_x, point_y = SortPoint(start_pt, point_x, point_y)
    pt_stack = Stack()
    pt_stack.push(0)
    pt_stack.push(1)
    for i in range(2, n):
        top = pt_stack.pop()
        while (CCW(point_x[pt_stack.peak()], point_y[pt_stack.peak()], point_x[top], point_y[top], point_x[i], point_y[i]) <= 0):
            top = pt_stack.pop()
        pt_stack.push(top)
        pt_stack.push(i)
    return pt_stack, point_x, point_y
    
# Display Final Result
def DisplayFinal(point_x, point_y):
    pt_stack, point_x, point_y = ConvexHull(point_x, point_y)
    n = pt_stack.size()
    pt_item = pt_stack.getitems()
    plt.scatter(point_x, point_y, 4)
    for i in range(n-1):
        plt.plot([point_x[pt_item[i]], point_x[pt_item[i+1]]],[point_y[pt_item[i]], point_y[pt_item[i+1]]], color = 'r')
    plt.plot([point_x[pt_item[n-1]], point_x[pt_item[0]]],[point_y[pt_item[n-1]], point_y[pt_item[0]]], color = 'r')
    plt.show()

DisplayFinal(point_x, point_y)