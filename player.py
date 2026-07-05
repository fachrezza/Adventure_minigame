import pygame
from settings import PLAYER_SPEED

FRAME_WIDTH = 64
FRAME_HEIGHT = 34
FRAME_COUNT = 5


class Player:

    def __init__(self):

        self.x = 480
        self.y = 220

        self.speed = PLAYER_SPEED

        self.direction = "down"
        self.state = "idle"

        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 6

        self.animations = {}

        self.load_animations()

    def load_animation(self, filename):

        sprite_sheet = pygame.image.load(filename).convert_alpha()

        frame_width = 64
        frame_height = 34

        frame_count = sprite_sheet.get_width() // frame_width

        frames = []

        for i in range(frame_count):

            frame = sprite_sheet.subsurface(
                pygame.Rect(
                    i * frame_width,
                    0,
                    frame_width,
                    frame_height
                )
            )

            frames.append(frame)

        return frames


    def load_animations(self):

        self.animations["idle_down"] = self.load_animation(
            "assets/player/idle_down.png"
        )

        self.animations["idle_up"] = self.load_animation(
            "assets/player/idle_up.png"
        )

        self.animations["idle_left"] = self.load_animation(
            "assets/player/idle_left.png"
        )

        self.animations["idle_right"] = self.load_animation(
            "assets/player/idle_right.png"
        )

        self.animations["walk_down"] = self.load_animation(
            "assets/player/walk_down.png"
        )

        self.animations["walk_up"] = self.load_animation(
            "assets/player/walk_up.png"
        )

        self.animations["walk_left"] = self.load_animation(
            "assets/player/walk_left.png"
        )

        self.animations["walk_right"] = self.load_animation(
            "assets/player/walk_right.png"
        )

    def update(self):

        keys = pygame.key.get_pressed()

        moving = False

        if keys[pygame.K_a]:
            self.x -= self.speed
            self.direction = "left"
            moving = True

        elif keys[pygame.K_d]:
            self.x += self.speed
            self.direction = "right"
            moving = True

        elif keys[pygame.K_w]:
            self.y -= self.speed
            self.direction = "up"
            moving = True

        elif keys[pygame.K_s]:
            self.y += self.speed
            self.direction = "down"
            moving = True


        if moving:
            self.state = "walk"

            self.animation_timer += 1

            if self.animation_timer >= self.animation_speed:

                self.animation_timer = 0

                self.current_frame += 1

                if self.current_frame >= FRAME_COUNT:
                    self.current_frame = 0

        else:

            self.state = "idle"

            self.animation_timer += 1

            if self.animation_timer >= self.animation_speed:

                self.animation_timer = 0

                self.current_frame += 1

                if self.current_frame >= FRAME_COUNT:
                    self.current_frame = 0
    
    def draw(self, screen, camera):

        screen_x = self.x - camera.x
        screen_y = self.y - camera.y

        animation_name = f"{self.state}_{self.direction}"
        animation = self.animations[animation_name]

        if self.current_frame >= len(animation):
            self.current_frame = 0

        image = animation[self.current_frame]

        screen.blit(image, (screen_x, screen_y))