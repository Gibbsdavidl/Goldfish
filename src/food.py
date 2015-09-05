__author__ = 'davidlgibbs'


__author__ = 'davidlgibbs'

import numpy as np
from graphics import *
import math

class Food():

    def __init__(self, win, title="Food pellet"):
        # where the food is located
        self.posX = int(np.random.randint(1,500,1)[0])
        self.posY = int(np.random.randint(1,500,1)[0])
        self.c = Circle(Point(self.posX,self.posY), 8)
        self.c.setOutline('black')
        self.c.setFill('green')
        self.c.draw(win)
        self.pointList = []
        self.gradient = []  # list of points
        self.r = [5, 10, 20, 40, 80] # each entry is a wave of food
        for ri in self.r:
            for t in range(0,360,45):
                x = ri*math.cos(t) + self.posX; # r is radius, t is angle, h,k are circle center
                y = ri*math.sin(t) + self.posY;
                self.pointList.append((x,y))
                self.gradient.append(Point(x,y))

    def draw(self, win):
        for pt in self.gradient:
            pt.draw(win)


    def getX(self):
        return(self.posX)

    def getY(self):
        return(self.posY)


    def newFood(self, win):
        #for pt in self.gradient:
        #    pt.undraw()
        self.c.undraw()
        self.posX = int(np.random.randint(1,500,1)[0])
        self.posY = int(np.random.randint(1,500,1)[0])
        self.c = Circle(Point(self.posX,self.posY), 8)
        self.c.setOutline('black')
        self.c.setFill('green')
        self.c.draw(win)
        self.pointList = []
        self.gradient = []  # list of points
        self.r = [5, 10, 20, 40, 80, 160, 320] # each entry is a wave of food
        for ri in self.r:
            for t in range(0,360,15):
                x = ri*math.cos(t) + self.posX; # r is radius, t is angle, h,k are circle center
                y = ri*math.sin(t) + self.posY;
                self.pointList.append((x,y))
                self.gradient.append(Point(x,y))
