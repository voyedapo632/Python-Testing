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
                sys.stdout.write(f"\033[{y};{x * 2 + 1}H" + self.pixels[self.width * y + x])
                sys.stdout.write(f"\033[{y};{x * 2}H" + self.pixels[self.width * y + x])

    def setColor(self, color):
        self.color = color

    def putPixel(self, x, y):
        if x < 0 or x >= self.width:
            return
        
        if y < 0 or y >= self.height:
            return

        self.pixels[self.width * int(y) + int(x)] = self.color

    def clear(self):
        for i in range(self.width * self.height):
            self.pixels[i] = self.color

    def drawRect(self, x, y, width, height):
        for _y in range(height):
            for _x in range(width):
                self.putPixel(x + _x, y + _y)

    def drawCircle(self, x, y, radius):
        for deg in range(360):
            cirX = int(x + radius * math.cos(math.radians(deg)))
            cirY = int(y + radius * math.sin(math.radians(deg)))
            self.putPixel(cirX, cirY)

    def drawLine(self, x1, y1, x2, y2, c1, c2):
        dx = x2 - x1
        dy = y2 - y1
        len = math.sqrt(dx**2 + dy**2)
        xi = dx / (len + 1)
        yi = dy / (len + 1)
        x, y = x1, y1

        oldColor = self.color
        dc = c2 - c1
        ci = dc / (len + 1)
        c = c1

        for i in range(int(len)):
            self.setColor(ASCIIShadeDark.get(c))
            self.putPixel(x, y)
            x += xi
            y += yi
            c += ci

        self.setColor(oldColor)

    def drawTriangle(self, x1, y1, x2, y2, x3, y3, c1, c2, c3):
        self.drawLine(x1, y1, x2, y2, c1, c2)
        self.drawLine(x2, y2, x3, y3, c2, c3)
        self.drawLine(x1, y1, x3, y3, c1, c3)

    def drawFillTriangle(self, x1, y1, x2, y2, x3, y3, c1, c2, c3):
        dx = x2 - x1
        dy = y2 - y1
        len = math.sqrt(dx**2 + dy**2)
        xi = dx / (len + 1)
        yi = dy / (len + 1)
        x, y = x1, y1

        oldColor = self.color
        dc = c2 - c1
        ci = dc / (len + 1)
        c = c1

        for i in range(int(len)):
            self.drawLine(x, y, x3, y3, c, c3)
            x += xi
            y += yi
            c += ci

        self.setColor(oldColor)