import Screen
import os
import ASCIIShadeDark

class App:
    def __init__(self):
        self.running = False
        self.scrn = Screen.Screen(60, 14)

    def start(self):
        os.system('clear')
        self.beginRender()

    def beginRender(self):
        self.running = True

        while self.running:
            self.draw()
            self.scrn.present()

    def draw(self):
        self.scrn.setColor(ASCIIShadeDark.get(0))
        self.scrn.clear()

        self.scrn.setColor(ASCIIShadeDark.get(7))
        self.scrn.drawRect(2, 2, 8, 4)

    def endRender(self):
        print("ENDED")
        self.running = False