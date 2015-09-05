__author__ = 'davidlgibbs'

from graphics import *
from fish import *
from food import *
import time

def main():
    print("run")
    win = GraphWin("Pond", 500, 500)
    #win.setBackground('blue')

    fish = Fish()
    fish.draw(win)

    food = Food(win)
    #food.draw(win)

    for i in range(0,1000):
        fish.step(food)
        fish.update(i, win)
        if fish.eat(food):
            food.newFood(win)
            #food.draw(win)
        update()
        time.sleep(0.2)


if __name__ == "__main__":
    main()
