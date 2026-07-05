import pygame

TILE_SIZE = 64

class World:

    def draw(self, screen, camera):

        for x in range(0, 3000, TILE_SIZE):

            pygame.draw.line(
                screen,
                (80, 160, 80),
                (x - camera.x, -camera.y),
                (x - camera.x, 3000 - camera.y)
            )

        for y in range(0, 3000, TILE_SIZE):

            pygame.draw.line(
                screen,
                (80, 160, 80),
                (-camera.x, y - camera.y),
                (3000 - camera.x, y - camera.y)
            )