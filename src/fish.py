__author__ = 'davidlgibbs'

import numpy as np
from graphics import *


class Fish():
    def __init__(self, title="Mr Fish"):
        self.posX = int(np.random.randint(1,500,1)[0])
        self.posY = int(np.random.randint(1,500,1)[0])
        self.velX = int(np.random.randint(-10,10,1)[0])
        self.velY = int(np.random.randint(-10,10,1)[0])
        self.initial_state = np.matrix([[self.posX],[self.velX],[self.posY],[self.velY]])
        self.c = Circle(Point(self.posX,self.posY), 8)
        self.c.setOutline('black')
        self.c.setFill('red')


        self.A = np.matrix([[1,1,0,0],[0,1,0,0],[0,0,1,1],[0,0,0,1]])    # State transition matrix.
        self.B = np.eye(4)                                               # Control matrix.
        self.control_vector = np.matrix([[0],[0],[0],[0]])

        self.H = np.eye(4)                                               # Observation matrix.
        self.P = np.eye(4)  *0.8                                             #

        self.Q = np.matrix([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])      # Estimated error in process.
        self.R = np.eye(4)*0.2                                           # Estimated error in measurements.
        self.current_state_estimate = self.initial_state    # Initial state estimate.
        self.current_prob_estimate = self.P  # Initial covariance estimate.


    def step(self, food):
        #---------------------------Measurement step-----------------------------
        xMeasure = float(food.getX() - self.posX) * abs(np.random.normal(0,2))
        yMeasure = float(food.getY() - self.posY) * abs(np.random.normal(0,2))
        measurement_vector = np.matrix([[self.posX], [xMeasure/10.0], [self.posY], [yMeasure/10.0]])
        control_vector = np.matrix([[0],[0],[0],[0]])

        #---------------------------Prediction step-----------------------------
        predicted_state_estimate = self.A * self.current_state_estimate + self.B * control_vector
        predicted_prob_estimate = (self.A * self.current_prob_estimate) * np.transpose(self.A) + self.Q

        #--------------------------Observation step-----------------------------
        innovation = measurement_vector - self.H*predicted_state_estimate
        innovation_covariance = self.H*predicted_prob_estimate*np.transpose(self.H) + self.R

        #-----------------------------Update step-------------------------------
        kalman_gain = predicted_prob_estimate * np.transpose(self.H) * np.linalg.inv(innovation_covariance)
        #self.current_state_estimate = predicted_state_estimate + kalman_gain * innovation
        self.current_state_estimate = predicted_state_estimate + innovation
        # We need the size of the matrix so we can make an identity matrix.
        size = self.current_prob_estimate.shape[0]
        # eye(n) = nxn identity matrix.
        self.current_prob_estimate = (np.eye(size)-kalman_gain*self.H)*predicted_prob_estimate
        self.posX = float(self.current_state_estimate[0][0])
        self.posY = float(self.current_state_estimate[2][0])
        self.velX = float(self.current_state_estimate[1][0])
        self.velY = float(self.current_state_estimate[3][0])


    def draw(self, win):
        self.c.draw(win)


    def update(self, i, win):
        self.posX += self.velX
        self.posY += self.velY
        if self.posX > 500 or self.posX < 0:
            self.velX = self.velX * -1
            if self.posX > 500: self.posX = 499
            if self.posX < 0:   self.posX = 1
            if self.velX > 10:  self.velX = 10
            if self.velY < -10: self.velY = -10
        if self.posY > 500 or self.posY < 0:
            self.velY = self.velY * -1
            if self.posY > 500: self.posY = 499
            if self.posY < 0:   self.posY = 1
            if self.velY > 10: self.velY = 10
            if self.velY < -10: self.velY = -10
        print("position: " + str(self.posX) + "  " + str(self.posY) + "   direction: " + str(self.velX) + "  " + str(self.velY) )
        self.c.move(self.velX, self.velY)


    def eat(self, food):
        if abs(food.getX()-self.posX) < 5 and abs(food.getY()-self.posY) < 5:
            return True
        else:
            return False


class Fish1():

    def __init__(self, title="Mr Fish"):
        self.posX = int(np.random.randint(1,500,1)[0])
        self.posY = int(np.random.randint(1,500,1)[0])
        self.dir = [int(np.random.randint(-10,10,1)[0]),int(np.random.randint(-10,10,1)[0])]
        self.c = Circle(Point(self.posX,self.posY), 3)
        self.c.setOutline('black')
        self.c.setFill('red')
        print(self.dir)

    def draw(self, win):
        self.c.draw(win)


    def update(self, i, win):
        self.posX += self.dir[0]
        self.posY += self.dir[1]
        if self.posX > 500 or self.posX < 0:
            self.dir[0] = self.dir[0] * -1
            if self.posX > 500: self.posX = 499
            if self.posX < 0:   self.posX = 1
            if self.dir[0] > 10:  self.dir[0] = 10
            if self.dir[1] < -10: self.dir[1] = -10
        if self.posY > 500 or self.posY < 0:
            self.dir[1] = self.dir[1] * -1
            if self.posY > 500: self.posY = 499
            if self.posY < 0:   self.posY = 1
            if self.dir[1] > 10: self.dir[1] = 10
            if self.dir[1] < -10: self.dir[1] = -10
        print("position: " + str(self.posX) + "  " + str(self.posY) + "   direction: " + str(self.dir[0]) + "  " + str(self.dir[1]) )
        self.c.move(self.dir[0], self.dir[1])
