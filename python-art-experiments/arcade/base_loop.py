#!/usr/bin/env python3

### First experiments with arcade - initiate the window, set up a base loop, draw simple things and then save images/gifs

import random

import arcade

width = 1000
height = 800
title = "test screen"

# Set up a class extending the basic arcade Window and override init, setup and draw (matching processing's setup/draw steps)
class SimpleWindow(arcade.Window):

    def __init__(self):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.csscolor.BEIGE)

    # do one-time/pre-start setup here
    def setup(self):
        self.agent = ShittyAgent(width/2, height/2, random.randrange(-2, 2), random.randrange(-2, 2))

    # every frame
    def on_draw(self):
        # in the future, try making svgs with pycairo here? also, shader stuff
        self.clear()
        self.agent.display()


# Just a really bad agent, just testing drawing a shitty thing.
class ShittyAgent():
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def next(self, t: int = 1):
        next_x = self.x + self.vx*t
        next_y = self.y + self.vy*t
        if next_x > width or 0 > next_x:
            self.vx = self.vx*-1
        if next_y > height or 0 > next_y:
            self.vy = self.vy*-1
        self.x = next_x
        self.y = next_y

    def display(self):
        self.next()
        arcade.draw_point(self.x, self.y, arcade.color.BLACK, 10)

def main():
    """Main function"""
    window = SimpleWindow()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
