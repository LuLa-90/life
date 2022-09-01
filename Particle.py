import random

class Particle:
    def __init__(self, width:int, heigth:int):
        self.newposX = random.randint(0, width)
        self.newposY = random.randint(0, heigth)
        self.posX = self.newposX
        self.posY = self.newposY
        # self.speedX = round((random.random() - 0.5)*2, 2)
        # self.speedY = round((random.random() - 0.5)*2, 2)

    def updateold(self):
        self.posX = self.newposX
        self.posY = self.newposY
