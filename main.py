import pygame
import random

num = random.randint(0, 100)
print(num)
W = 480
H = 360
SILVER = (192, 192, 192)
BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption("угадай число ")
screen = pygame.display.set_mode((W, H))
pygame.mouse.set_visible(False)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False