import pygame


class Pawn(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        if image == "white":
            self.image = pygame.image.load('Resources/whitePawn.png')
        else:
            self.image = pygame.image.load('Resources/blackPawn.png')

        self.rect = self.image.get_rect()
        self.color = image

    def setPawnPosition(self, mx, my):
        self.rect.x = mx
        self.rect.y = my

    def movePawn(self, mx, my, chessTilesSprintTable: pygame.sprite.Group):
        for tileSprite in chessTilesSprintTable:
            if tileSprite.rect.collidepoint((mx, my)):
                self.rect.x = tileSprite.getTileCenterX(self)
                self.rect.y = tileSprite.getTileCenterY(self)
