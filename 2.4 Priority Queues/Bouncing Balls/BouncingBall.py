import pygame as pg
import _thread
# import threading
import random
import math
import time
import cv2
import numpy as np

# global param
R = 10
window = [600, 600]
Rect = [int(window[0]*0.05), int(window[1]*0.05), int(window[0]*0.95), int(window[1]*0.95)]
# Rect = [30, 30, 330, 330]
Rect_line = 5
init_speed_max = 50
mass = 0.5
num_of_ball = 200
COLOR_RED = (20, 20, 190)
COLOR_GREY = (50, 50, 50)
color_change = True
rand_rate = 0.15

class MinPQ:
    # In the Binary heap, k's parent is k/2(int), k's child is 2*k and 2*k+1
    # Note that the index of the root is 1 
    def __init__(self):
        # Initialize
        self.key = [None]
        self.N = 0
    
    def isEmpty(self):
        return self.N == 0
    
    def insert(self, key):
        # Insert a key to the end
        self.N += 1
        # self.key[self.N] = key
        self.key.append(key)
        self.swim(self.N)
    
    def delMin(self):
        # Get the minKey
        minKey = self.key[1]
        # Exchange the root with the end
        self.exch(1, self.N)
        # Delete the end
        self.key.pop(self.N)
        self.N -= 1
        # Sink Approach to keep the order of the heap
        self.sink(1)
        return minKey

    def Min(self):
        return self.key[1]

    def swim(self, k):
        while k > 1 and self.more(int(k/2), k):
            self.exch(k, int(k/2))
            k = int(k/2)

    def sink(self, k):
        # Remember to include the equal condition
        while(2 * k <= self.N):
            # Find the less child
            j = 2 * k
            if j < self.N and self.more(j, j + 1):
                j += 1
            # Compare the less child with parent
            if not self.more(k, j):
                break
            self.exch(k, j)
            # set k = j to iterate
            k = j
    
    def exch(self, i, j):
        self.key[i], self.key[j] = self.key[j], self.key[i]
    
    def more(self, i, j):
        if self.key[i].compareTo(self.key[j]) > 0:
            return True
        else:
            return False
'''
class Draw:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((Rect[2] - Rect[0], Rect[3] - Rect[1]))
        self.screen.fill((245, 245, 245))
        pg.display.set_caption("Bouncing Balls")
        self.R = R
        self.Grey = 50, 50, 50
        pg.draw.rect(self.screen, self.Grey, (Rect[0], Rect[1], Rect[2], Rect[3]), Rect_line)
        pg.display.update()

    def drawBalls(self, balls):
        self.screen.fill((245, 245, 245))
        pg.draw.rect(self.screen, self.Grey, (Rect[0], Rect[1], Rect[2], Rect[3]), Rect_line)
        for ball in balls:
             # _thread.start_new_thread(self.drawBallThread, (ball, ))
             pg.draw.circle(self.screen, self.Grey, (round(ball.rx), round(ball.ry)), self.R)
        pg.display.update()

    def drawBallThread(self, ball):
        pg.draw.circle(self.screen, self.Grey, (round(ball.rx), round(ball.ry)), self.R)
'''
class Draw:
    def __init__(self):
        # Create background
        # self.bg_img = np.zeros((int(abs(Rect[2] - Rect[0])*1.2), int(abs(Rect[3] - Rect[1])*1.2), 3), np.uint8)
        self.bg_img = np.zeros((window[0], window[1], 3), np.uint8)
        self.bg_img += 245
        cv2.rectangle(self.bg_img, (Rect[0], Rect[1]), (Rect[2], Rect[3]), (50, 50, 50), 5)
        cv2.namedWindow("Bouncing balls", 0)
        cv2.imshow("Bouncing balls", self.bg_img)
        cv2.waitKey(1)

    def drawBalls(self, balls):
        img = self.bg_img.copy()
        for ball in balls:
            cv2.circle(img, (round(ball.rx), round(ball.ry)), R, ball.color, -1)
        cv2.imshow("Bouncing balls", img)
        cv2.waitKey(1)
        
class Ball:
    def __init__(self):
        # position
        self.rx, self.ry = random.uniform(Rect[0] + 2*R, Rect[2] - 2*R), random.uniform(Rect[1] + 2*R, Rect[3] - 2*R)
        # velocity
        self.vx, self.vy = random.uniform(-init_speed_max, init_speed_max), random.uniform(-init_speed_max, init_speed_max)
        # radius
        self.radius = R
        # mass
        self.mass = mass
        # number of collisions
        self.count = 0
        # color of ball
        self.color = COLOR_GREY

    def Move(self, dt):
        self.rx = self.rx + dt * self.vx
        self.ry = self.ry + dt * self.vy 
    
    def timeToHit(self, that):
        if self == that:
            return None
        dx, dy = that.rx - self.rx, that.ry - self.ry
        dvx, dvy = that.vx - self.vx, that.vy - self.vy
        dvdr = dx * dvx + dy * dvy
        if dvdr > 0:
            return None
        dvdv = dvx * dvx + dvy * dvy
        drdr = dx * dx + dy * dy
        sigma = self.radius + that.radius
        d = dvdr * dvdr - dvdv * (drdr - sigma * sigma)
        if d < 0 or dvdv == 0:
            return None
        time = -(dvdr + math.sqrt(d)) / dvdv
        if time <= 0:
            return None
        return time
    
    def timeToHitVerticalWall(self):
        if self.vx > 0:
            time = (Rect[2] - self.rx - self.radius) / self.vx
        elif self.vx < 0:
            time = (Rect[0] - self.rx + self.radius) / self.vx
        elif self.vx == 0:
            return None
        if time <= 0:
            return None
        return time

    def timeToHitHorizontalWall(self):
        if self.vy > 0:
            time = (Rect[3] - self.ry - self.radius) / self.vy
        elif self.vy < 0:
            time = (Rect[1] - self.ry + self.radius) / self.vy
        elif self.vy == 0:
            return None
        if time <= 0:
            return None
        return time
    
    def bounceOff(self, that):
        dx, dy = that.rx - self.rx, that.ry - self.ry
        dvx, dvy = that.vx - self.vx, that.vy - self.vy
        dvdr = dx * dvx + dy * dvy
        dist = self.radius + that.radius
        J = 2 * self.mass * that.mass * dvdr / ((self.mass + that.mass) * dist)
        Jx = J * dx / (dist)
        Jy = J * dy / (dist)
        self.vx += Jx / self.mass
        self.vy += Jy / self.mass
        that.vx -= Jx / that.mass
        that.vy -= Jy / that.mass
        self.count += 1
        that.count += 1
        if color_change:
            if self.color == COLOR_RED or that.color == COLOR_RED:
                rate = random.uniform(0, 1)
                if rate < rand_rate:
                    that.color = COLOR_RED
                    self.color = COLOR_RED
    
    def bounceOffVerticalWall(self):
        self.vx = -self.vx
        self.count += 1

    def bounceOffHorizontalWall(self):
        self.vy = -self.vy
        self.count += 1
    
class Event:
    def __init__(self, time, ballA, ballB, ballA_c, ballB_c):
        self.time = time
        self.ballA = ballA
        self.ballB = ballB
        self.ballA_c = ballA_c
        self.ballB_c = ballB_c
    
    def compareTo(self, that):
        return self.time - that.time

    def isValid(self):
        if self.ballA == None:
            if self.ballB == None:
                return False
            if self.ballB.count == self.ballB_c:
                return True
            return False
        if self.ballA.count == self.ballA_c and self.ballB == None:
            return True
        if self.ballA.count == self.ballA_c and self.ballB.count == self.ballB_c:
            return True
        return False

class CollisionSystem:
    def __init__(self, N):
        self.pq = MinPQ()
        self.t = 0.0
        self.balls = []
        self.N = N
        self.draw = Draw()
        self.timeseq = 0.3
        for i in range(N):
            self.balls.append(Ball())
    
    def predict(self, ball):
        if ball == None:
            return
        # Time to hit another ball
        for i in range(self.N):
            dt = ball.timeToHit(self.balls[i])
            if dt:
                self.pq.insert(Event(self.t + dt, ball, self.balls[i], ball.count, self.balls[i].count))
        # Time to Hit the walls
        dt = ball.timeToHitVerticalWall()
        if dt:
            self.pq.insert(Event(self.t + dt, ball, None, ball.count, None))
        dt = ball.timeToHitHorizontalWall()
        if dt:
            self.pq.insert(Event(self.t + dt, None, ball, None, ball.count))
    
    def simulate(self):
        for i in range(self.N):
            self.predict(self.balls[i])
        if color_change:
            self.balls[1].color = COLOR_RED
        while not self.pq.isEmpty():
            next_event = self.pq.Min()
            if next_event.time - self.t <= self.timeseq:
                event = self.pq.delMin()
                if not event.isValid():
                    continue
                BallA, BallB = event.ballA, event.ballB
                # Move all the balls to event time
                for i in range(self.N): 
                    self.balls[i].Move(event.time - self.t)
                self.redraw()
                # Event occurs
                dt = event.time - self.t
                self.t = event.time
                # Handle the event
                if BallA != None and BallB != None:
                    BallA.bounceOff(BallB)
                elif BallA != None and BallB == None:
                    BallA.bounceOffVerticalWall()
                elif BallA == None and BallB != None:
                    BallB.bounceOffHorizontalWall()
                # re-predict Ball A and B
                self.predict(BallA)
                self.predict(BallB)
                time.sleep(0.001)
            else:
                # Move all the balls
                for i in range(self.N): 
                    self.balls[i].Move(self.timeseq)
                self.redraw()
                self.t = self.t + self.timeseq
                time.sleep(0.001)
            
    def redraw(self):
        self.draw.drawBalls(self.balls)


# Test Demo
if __name__ == '__main__':
    BCS = CollisionSystem(num_of_ball)
    BCS.simulate()
    # _thread.start_new_thread(BCS.simulate())
    print("Finished!")
            




        
