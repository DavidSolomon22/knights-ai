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

        self.rect.x
        self.rect.y

    def setPawnPosition(self, mx, my):
        self.rect.x = mx
        self.rect.y = my

    def PawnSelected(self):
        self.image = self.chosenPawnImage

    def PawnUnselected(self):
        self.image = self.defaultPawnImage

    def getTileCenterX(self):
        return int(self.rect.x + (self.image.get_width()) / 2)

    def getTileCenterY(self):
        return int(self.rect.y + (self.image.get_height()) / 2)

    def checkIfPawnIsMovingToTheNearestTile(self, newPawnTile: pygame.sprite.Sprite):
        distanceX = abs(newPawnTile.getTileCenterX() - self.getTileCenterX())
        distanceY = abs(newPawnTile.getTileCenterY() - self.getTileCenterY())
        print(distanceX)
        print(distanceY)

        if (distanceX == newPawnTile.image.get_width()) ^ (distanceY == newPawnTile.image.get_height()):
            if (distanceX > newPawnTile.image.get_width()) or (distanceY > newPawnTile.image.get_height()):
                return False
            return True
        else:
            return False

    def checkIfPawnIsJumpingOver(self, newPawnTile: pygame.sprite.Sprite):
        distanceX = abs(newPawnTile.getTileCenterX() - self.getTileCenterX())
        distanceY = abs(newPawnTile.getTileCenterY() - self.getTileCenterY())

        if (distanceX == (newPawnTile.image.get_width() * 2)) ^ (distanceY == (newPawnTile.image.get_height() * 2)):
            if (distanceX == newPawnTile.image.get_width()) or (distanceY == newPawnTile.image.get_height()):
                return False
            return True
        else:
            return False


    def movePawn(self, mx, my, chessTilesSprintTable: pygame.sprite.Group, pawnsSprintTable: pygame.sprite.Group):
        for tileSprite in chessTilesSprintTable:
            if tileSprite.rect.collidepoint((mx, my)):
                if self.checkIfPawnIsMovingToTheNearestTile(tileSprite):
                    if tileSprite.checkIfContainsPawn(pawnsSprintTable):
                        self.rect.x = tileSprite.getTileCenterXForDrawingPawn(self)
                        self.rect.y = tileSprite.getTileCenterYForDrawingPawn(self)
                        return True
                    else:
                        return False
                else:
                    if tileSprite.checkIfContainsPawn(pawnsSprintTable):
                        if self.checkIfPawnIsJumpingOver(tileSprite):
                            print('Double jump possible')
                        else:
                            print('Double jump not possible')
                            return False
                    else:
                        print("pawn 2 tiles away")
                        return False


