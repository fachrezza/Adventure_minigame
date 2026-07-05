import pygame
from settings import PLAYER_SPEED

class Player:

    def __init__(self):

        self.x = 480
        self.y = 220

        self.width = 32
        self.height = 48

        self.speed = PLAYER_SPEED

        self.color = (pygame.Color('blue'))

    def update(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x -= self.speed

        if keys[pygame.K_d]:
            self.x += self.speed

        if keys[pygame.K_w]:
            self.y -= self.speed

        if keys[pygame.K_s]:
            self.y += self.speed

    def draw(self, screen, camera):

        screen_x = self.x - camera.x
        screen_y = self.y - camera.y

        pygame.draw.rect(
            screen,
            self.color,
            (screen_x, screen_y, self.width, self.height)
        )