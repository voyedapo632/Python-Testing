import Screen
import os
import ASCIIShadeDark

class App:
    def __init__(self):
        self.running = False
        self.scrn = Screen.Screen(50, 30)

    def start(self):
        os.system('clear')
        self.beginRender()

    def beginRender(self):
        self.running = True

        while self.running:
            self.draw()
            self.scrn.present()

    def draw2D(self):
        # Clear screen
        self.scrn.setColor(ASCIIShadeDark.get(0))
        self.scrn.clear()

        # Ractangle
        self.scrn.setColor(ASCIIShadeDark.get(3))
        self.scrn.drawRect(2, 2, 8, 8)

        # Circle
        self.scrn.setColor(ASCIIShadeDark.get(5))
        self.scrn.drawCircle(16, 6, 4)

        # Line
        self.scrn.setColor(ASCIIShadeDark.get(4))
        self.scrn.drawLine(12, 12, 20, 20)

        # Triangle
        self.scrn.setColor(ASCIIShadeDark.get(2))
        self.scrn.drawTriangle(22, 22, 36, 23, 30, 12)



    def draw3D(self):
        pass

    def endRender(self):
        print("ENDED")
        self.running = False