import pygame
import sys

from settings import *
from player import Player
from camera import Camera
from world import World



pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Adventure Minigame")

camera = Camera()
world = World()

clock = pygame.time.Clock()

player = Player()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()

    camera.update(player)

    screen.fill(BACKGROUND_COLOR)

    world.draw(screen, camera)

    player.draw(screen, camera)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()