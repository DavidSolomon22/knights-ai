import pygame
import Pawn


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

    def getTileCenterX(self, objectSprite):
        tileX = self.rect.x + (self.image.get_width() - objectSprite.image.get_width()) / 2
        return tileX

    def getTileCenterY(self, objectSprite):
        tileY = self.rect.y + (self.image.get_width() - objectSprite.image.get_height()) / 2
        return tileY

    def checkIfContainsPawn(self, mx, my, pawnsSprintTable: pygame.sprite.Group):
        for pawnSprint in pawnsSprintTable:
            if pawnSprint.rect.collidepoint((self.getTileCenterX(pawnSprint), self.getTileCenterY(pawnSprint))):
                return False
        return True
