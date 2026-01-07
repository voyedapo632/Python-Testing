from Screen import Screen
import os
import ASCIIShadeDark
import numpy as np
import math

class App:
    def __init__(self):
        self.running = False
        self.scrn = Screen(50, 30)
        self.rot = 0.0;

    def start(self):
        os.system('clear')
        self.beginRender()

    def beginRender(self):
        self.running = True

        while self.running:
            # self.draw2D()
            self.draw3D()
            self.scrn.present()
            self.rot += 0.03

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
        self.scrn.drawLine(12, 12, 20, 20, 1, 7)

        # Triangle
        self.scrn.drawTriangle(22, 22, 36, 23, 30, 12, 1, 3, 7)

    def toScreenPoint(self, x, y, z):
        halfWidth = self.scrn.width / 2.0
        halfHeight = self.scrn.height / 2.0
        return [halfWidth + halfWidth * x, 
                halfHeight + halfHeight * -y, z]

    def translateVertex(self, vertex:np.array, value:list):
        vertex += value

    def scaleVertex(self, vertex:np.array, value:list):
        vertex *= value

    def rotateVertex(self, vertex:np.array, value:list):
        xMatrix = np.transpose(np.array([np.dot([1.0, 0.0, 0.0], vertex),
                                         np.dot([0.0, math.cos(value[0]), -math.sin(value[0])], vertex),
                                         np.dot([0.0, math.sin(value[0]), math.cos(value[0])], vertex)]))
        vertex[0] = xMatrix[0]
        vertex[1] = xMatrix[1]
        vertex[2] = xMatrix[2]

    def draw3D(self):
        # Clear screen
        self.scrn.setColor(ASCIIShadeDark.get(0))
        self.scrn.clear()

         # Verticies
        verticies = [
            # Position           Color
            [[-1.0, -1.0, -1.0], [2, 0, 0]],
            [[1.0, -1.0, -1.0],  [3, 0, 0]],
            [[1.0, 1.0, -1.0],   [4, 0, 0]],
            [[-1.0, 1.0, -1.0],  [3, 0, 0]],
            [[-1.0, -1.0, 1.0],  [4, 0, 0]],
            [[1.0, -1.0, 1.0],   [5, 0, 0]],
            [[1.0, 1.0, 1.0],    [6, 0, 0]],
            [[-1.0, 1.0, 1.0],   [1, 0, 0]],
        ]

        # Indices
        indices = [
            [0, 1, 2],
            [0, 2, 3],

            [4, 5, 6],
            [4, 6, 7],

            [0, 4, 7],
            [0, 3, 7],

            [1, 5, 6],
            [1, 2, 6],

            [0, 1, 5],
            [0, 4, 5],

            [3, 2, 6],
            [3, 7, 6],
        ]

        # Model Transformation
        modelTranslation = [0.0, 0.0, 2.5]
        modelScale = [1.0, 1.0, 1.0]
        modelRotation = [self.rot, 0.0, 0.0]

        # Projection
        aspectRatio = float(self.scrn.height) / float(self.scrn.width)

        for tri in indices:
            v1 = np.array(verticies[tri[0]][0])
            v2 = np.array(verticies[tri[1]][0])
            v3 = np.array(verticies[tri[2]][0])
            c1 = np.array(verticies[tri[0]][1])
            c2 = np.array(verticies[tri[1]][1])
            c3 = np.array(verticies[tri[2]][1])

            # Rotation
            self.rotateVertex(v1, modelRotation)
            self.rotateVertex(v2, modelRotation)
            self.rotateVertex(v3, modelRotation)

            # Translate
            self.translateVertex(v1, modelTranslation)
            self.translateVertex(v2, modelTranslation)
            self.translateVertex(v3, modelTranslation)

            # Scale
            self.scaleVertex(v1, modelScale)
            self.scaleVertex(v2, modelScale)
            self.scaleVertex(v3, modelScale)
           
            if v1[2] > 0.0:
                v1[0] /= v1[2]
                v1[1] /= v1[2]
            
            if v2[2] > 0.0:
                v2[0] /= v2[2]
                v2[1] /= v2[2]
            
            if v3[2] > 0.0:
                v3[0] /= v3[2]
                v3[1] /= v3[2]

            sv1 = self.toScreenPoint(v1[0] * aspectRatio, v1[1], v1[2])
            sv2 = self.toScreenPoint(v2[0] * aspectRatio, v2[1], v2[2])
            sv3 = self.toScreenPoint(v3[0] * aspectRatio, v3[1], v3[2])

            self.scrn.drawFillTriangle(int(sv1[0]), int(sv1[1]),
                                   int(sv2[0]), int(sv2[1]),
                                   int(sv3[0]), int(sv3[1]),
                                   c1[0], c2[0], c3[0])

    def endRender(self):
        print("ENDED")
        self.running = False