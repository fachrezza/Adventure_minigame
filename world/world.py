import pygame
import pytmx


class World:

    def __init__(self):

        self.tmx = pytmx.load_pygame(
            "assets/maps/world.tmx"
        )

    def draw(self, screen, camera):

        for layer in self.tmx.visible_layers:

            if hasattr(layer, "tiles"):

                for x, y, image in layer.tiles():

                    screen.blit(
                        image,
                        (
                            x * self.tmx.tilewidth - camera.x,
                            y * self.tmx.tileheight - camera.y
                        )
                    )