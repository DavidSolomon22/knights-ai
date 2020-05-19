import pygame


class Pawn(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.chosenPawnImage = pygame.image.load('Resources/chosenPawn.png')

        if image == "white":
            self.color = pygame.image.load('Resources/whitePawn.png')
        else:
            self.color = pygame.image.load('Resources/blackPawn.png')
        self.image = self.color

        self.rect = self.image.get_rect()

    def setPawnPosition(self, mx, my):
        self.rect.x = mx
        self.rect.y = my

    def PawnClicked(self):
        self.image = self.chosenPawnImage

    def PawnUnclicked(self):
        self.image = self.color

    def movePawn(self, mx, my, chessTilesSprintTable: pygame.sprite.Group, pawnsSprintTable: pygame.sprite.Group):
        for tileSprite in chessTilesSprintTable:
            if tileSprite.rect.collidepoint((mx, my)):
                if tileSprite.checkIfContainsPawn(mx, my, pawnsSprintTable):
                    self.rect.x = tileSprite.getTileCenterX(self)
                    self.rect.y = tileSprite.getTileCenterY(self)
                # elif:
