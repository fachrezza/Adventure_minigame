from settings import WIDTH, HEIGHT, WORLD_WIDTH, WORLD_HEIGHT

class Camera:

    def __init__(self):
        self.x = 0
        self.y = 0

    def update(self, player):

        self.x = player.x - WIDTH // 2
        self.y = player.y - HEIGHT // 2

        if self.x < 0:
            self.x = 0

        if self.y < 0:
            self.y = 0

        if self.x > WORLD_WIDTH - WIDTH:
            self.x = WORLD_WIDTH - WIDTH

        if self.y > WORLD_HEIGHT - HEIGHT:
            self.y = WORLD_HEIGHT - HEIGHT