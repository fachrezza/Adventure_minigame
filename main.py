import pygame
import sys

from settings import *
from player import Player

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Adventure Minigame")

clock = pygame.time.Clock()

player = Player()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()

    screen.fill(BACKGROUND_COLOR)

    player.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()