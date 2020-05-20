import pygame


class Pawn(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()

        if image == "white":
            self.defaultPawnImage = pygame.image.load('Resources/whitePawn.png')
            self.chosenPawnImage = pygame.image.load('Resources/chosenPawn.png')
            self.color = image
        else:
            self.defaultPawnImage = pygame.image.load('Resources/blackPawn.png')
            self.chosenPawnImage = pygame.image.load('Resources/chosenPawn.png')
            self.color = image
        self.image = self.defaultPawnImage

        self.rect = self.image.get_rect()

    def setPawnPosition(self, mx, my):
        self.rect.x = mx
        self.rect.y = my

    def PawnSelected(self):
        self.image = self.chosenPawnImage

    def PawnUnselected(self):
        self.image = self.defaultPawnImage

    def movePawn(self, mx, my, chessTilesSprintTable: pygame.sprite.Group, pawnsSprintTable: pygame.sprite.Group):
        for tileSprite in chessTilesSprintTable:
            if tileSprite.rect.collidepoint((mx, my)):
                if tileSprite.checkIfContainsPawn(mx, my, pawnsSprintTable):
                    self.rect.x = tileSprite.getTileCenterX(self)
                    self.rect.y = tileSprite.getTileCenterY(self)



