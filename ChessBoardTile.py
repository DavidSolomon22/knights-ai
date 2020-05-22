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

    def getTileCenterX(self):
        return int(self.rect.x + self.image.get_width() / 2)

    def getTileCenterY(self):
        return int(self.rect.y + self.image.get_height() / 2)

    def getTileCenterXForDrawingPawn(self, objectSprite):
        tileX = int(self.rect.x + (self.image.get_width() - objectSprite.image.get_width()) / 2)
        return tileX

    def getTileCenterYForDrawingPawn(self, objectSprite):
        tileY = int(self.rect.y + (self.image.get_height() - objectSprite.image.get_height()) / 2)
        return tileY

    def checkIfContainsPawn(self, pawnsSprintTable: pygame.sprite.Group):
        for pawnSprint in pawnsSprintTable:
            if pawnSprint.rect.collidepoint(
                    (self.getTileCenterXForDrawingPawn(pawnSprint), self.getTileCenterYForDrawingPawn(pawnSprint))):
                return False
        return True
