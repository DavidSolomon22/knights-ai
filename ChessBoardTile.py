import pygame

class ChessBoardTile(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        # rectangle to detect collisions
        self.rect = self.image.get_rect()

    def setTilePosition(self, mx, my):
        self.rect.x = mx
        self.rect.y = my
