import pygame
import math
import random
pygame.init()
pygame.display.set_caption("Pumpkins!")
screen = pygame.display.set_mode((800, 800))
screen.fill((0, 0, 0))


BLACK = (0,0,0)
ORANGE = (200, 100, 0)
GREEN = (0,150, 0)
patch = []
class BruhKin:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def draw(self):
        pygame.draw.rect(screen, (GREEN), (self.xpos-10, self.ypos-70, 20, 25))
        pygame.draw.circle(screen, (ORANGE), (self.xpos, self.ypos), 50)
        pygame.draw.arc(screen, (BLACK), (self.xpos-15,self.ypos,30,20), math.pi, math.pi*2, 5)
        pygame.draw.arc(screen, (BLACK), (self.xpos-25,self.ypos-20,20,20), 0, math.pi, 5)
        pygame.draw.arc(screen, (BLACK), (self.xpos,self.ypos-20,20,20), 0, math.pi, 5)

#patch = [BruhKin(random.randrange(0,700)


#create the pumkins
Swag = BruhKin(random.randrange(0,700), random.randrange(0,700))
Swag2 = BruhKin(random.randrange(0,700), random.randrange(0,700))
Swag3 = BruhKin(random.randrange(0,700), random.randrange(0,700))

#push into list
patch.append(Swag)
patch.append(Swag2)
patch.append(Swag3)


for i in patch:
    i.draw()
   
   
#Swag.draw()
#Swag2.draw()
#Swag3.draw()


pygame.display.flip()
