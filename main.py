import pygame 
import sys 
import math 
from fisics import fisics
pygame.init()
print('run')
size = (800,600)
white = (255,255,255)
screen_info=pygame.display.Info()

screen = pygame.display.set_mode(size)
pygame.display.set_caption('fisics')

freeze_moment =False
position = (10,10)
fisics = fisics(position,acceleration_x=10)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))
    fisics.set_move_x()
    postion = fisics.update()
    pygame.draw.circle(screen,white,postion,5)

    pygame.display.flip()
    pygame.time.Clock().tick(30)