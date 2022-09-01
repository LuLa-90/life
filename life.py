# 

from dis import dis
import pygame
import random
import math
from Particle import *
from typing import List

# -------------------------- PREMENNE --------------------------

FPS=60
width = 1000
height = 700

# -------------------- DEFINOVANIE FUNKCII -------------------------

def main():
    # global
    global pos
    
    # premenne
    run=True
    gamestate=0

    yellows = create(50)
    cyans = create(50)
    
    # hlavny FPS clock
    clock = pygame.time.Clock()
    
    # main loop
    while run == True:
        window.fill('#10051c')

        # game
        if gamestate == 0:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    break

            applyrules(yellows, (255,255,0))
            applyrules(cyans, (0,255,255))
            for p1 in yellows:
                rule(p1, cyans, 0.1)
                rule(p1, yellows, -0.04)
            for p1 in cyans:
                rule(p1, yellows, 0.1)
        
                    
        clock.tick(FPS)
        pygame.display.update()
                
# ---------------------------- FUNKCIE -----------------------------
def create(count:int):
    list:List[Particle] = []
    for i in range(count):
            particle = Particle(width, height)
            list.append(particle)
    return list

def applyrules(list:List[Particle], color):
    for particle in list:
                # particle.posX += particle.speedX
                # particle.posY += particle.speedY
                # borderrule(particle)

                pygame.draw.rect(window, color, pygame.Rect(particle.newposX-2, particle.newposY-2, 4, 4))
                particle.updateold()

def rule(part1:Particle, list:List[Particle], g:float):
    fx = 0
    fy = 0
    
    for part2 in list:
        dx = part1.posX - part2.posX
        dy = part1.posY - part2.posY

        dist = math.sqrt(dx**2 + dy**2)

        if dist > 0 and dist < 150:
            F = g * 1/dist
            fx += F * dx
            fy += F * dy

    part1.newposX += fx
    part1.newposY += fy

def borderrule(part:Particle):
    if part.newposX < 100:
        part.speedX += 0.02 * (100/part.newposX)
    elif part.newposX > width-100:
        part.speedX -= 0.02 * (100/(width-part.newposX))
    if part.newposY < 100:
        part.speedY += 0.02 * (100/part.newposY)
    elif part.newposY > height-100:
        part.speedY -= 0.02 * (100/(height-part.newposY))

# -------------------------- INICIALIZACIA --------------------------
# inicializacia pygame a fontov
pygame.init()

# nahodny seed podla casu
random.seed()

# vytvor okno s captionom
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Life")

# -------------------- SPUSTENIE APLIKACIE --------------------------
main()