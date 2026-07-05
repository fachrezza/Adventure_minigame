import pygame
import sys

from settings import *
from player import Player
from camera import Camera
from world import World

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Adventure Minigame")

clock = pygame.time.Clock()

camera = Camera()
world = World()
player = Player()

running = True

while running:

    # Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    player.update()
    camera.update(player)

    # Draw
    screen.fill(BACKGROUND_COLOR)

    world.draw(screen, camera)
    player.draw(screen, camera)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()