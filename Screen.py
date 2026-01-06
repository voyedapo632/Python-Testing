import sys
import math
import ASCIIShadeDark

class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = ASCIIShadeDark.get(0)
        self.pixels = [self.color] * width * height

    def present(self):
        for y in range(self.height):
            for x in range(self.width):
                sys.stdout.write(f"\033[{y};{x}H" + self.pixels[self.width * y + x])

    def setColor(self, color):
        self.color = color

    def putPixel(self, x, y):
        if x < 0 or x >= self.width:
            return
        
        if y < 0 or y >= self.height:
            return

        self.pixels[self.width * y + x] = self.color

    def clear(self):
        for i in range(self.width * self.height):
            self.pixels[i] = self.color

    def drawRect(self, x, y, width, height):
        for _y in range(height):
            for _x in range(width):
                self.putPixel(x + _x, y + _y)
                
    def drawLine(self, x1, y1, x2, y2):
        pass