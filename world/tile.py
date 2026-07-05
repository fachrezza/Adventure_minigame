import pygame


class Tile:

    SIZE = 32

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.image = None

    def draw(self, screen, camera):

        screen_x = self.x - camera.x
        screen_y = self.y - camera.y

        if self.image:
            screen.blit(self.image, (screen_x, screen_y))
        else:
            pygame.draw.rect(
                screen,
                (80, 170, 80),
                (screen_x, screen_y, self.SIZE, self.SIZE)
            )