import pygame


class Pawn(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()

        if image == "white":
            self.defaultPawnImage = pygame.image.load('resources/white_pawn.png')
            self.chosenPawnImage = pygame.image.load('resources/chosen_pawn.png')
            self.color = image
        else:
            self.defaultPawnImage = pygame.image.load('resources/black_pawn.png')
            self.chosenPawnImage = pygame.image.load('resources/chosen_pawn.png')
            self.color = image
        self.image = self.defaultPawnImage
        self.rect = self.image.get_rect()

    def set_pawn_position(self, mx, my):
        self.rect.x = mx
        self.rect.y = my

    def pawn_selected(self):
        self.image = self.chosenPawnImage

    def pawn_unselected(self):
        self.image = self.defaultPawnImage

    def get_tile_center_x(self):
        return int(self.rect.x + (self.image.get_width()) / 2)

    def get_tile_center_y(self):
        return int(self.rect.y + (self.image.get_height()) / 2)

    def check_if_pawn_is_moving_to_the_nearest_tile(self, newPawnTile: pygame.sprite.Sprite):
        distanceX = abs(newPawnTile.get_tile_center_x() - self.get_tile_center_x())
        distanceY = abs(newPawnTile.get_tile_center_y() - self.get_tile_center_y())

        if (distanceX == newPawnTile.image.get_width()) ^ (distanceY == newPawnTile.image.get_height()):
            if (distanceX > newPawnTile.image.get_width()) or (distanceY > newPawnTile.image.get_height()):
                return False
            return True
        else:
            return False

    def check_if_pawn_is_jumping_over(self, newPawnTile: pygame.sprite.Sprite):
        distanceX = abs(newPawnTile.get_tile_center_x() - self.get_tile_center_x())
        distanceY = abs(newPawnTile.get_tile_center_y() - self.get_tile_center_y())

        if (distanceX == (newPawnTile.image.get_width() * 2)) ^ (distanceY == (newPawnTile.image.get_height() * 2)):
            if (distanceX == newPawnTile.image.get_width()) or (distanceY == newPawnTile.image.get_height()):
                return False
            return True
        else:
            return False

    def double_jump(self, newPawnTile: pygame.sprite.Sprite, pawnsSprintTable: pygame.sprite.Group):
        distanceX = newPawnTile.get_tile_center_x() - self.get_tile_center_x()
        distanceY = newPawnTile.get_tile_center_y() - self.get_tile_center_y()

        if distanceX != 0:
            if distanceX > 0:
                pawnInBettwenX = newPawnTile.get_tile_center_x_for_drawing_pawn(self) - newPawnTile.image.get_width()
                for pawn in pawnsSprintTable:
                    if pawn.rect.x == pawnInBettwenX and pawn.rect.y == self.rect.y:
                        return True
            else:
                pawnInBettwenX = newPawnTile.get_tile_center_x_for_drawing_pawn(self) + newPawnTile.image.get_width()
                for pawn in pawnsSprintTable:
                    if pawn.rect.x == pawnInBettwenX and pawn.rect.y == self.rect.y:
                        return True
        else:
            if distanceY > 0:
                pawnInBettwenY = newPawnTile.get_tile_center_y_for_drawing_pawn(self) - newPawnTile.image.get_height()
                for pawn in pawnsSprintTable:
                    if pawn.rect.y == pawnInBettwenY and pawn.rect.x == self.rect.x:
                        return True
            else:
                pawnInBettwenY = newPawnTile.get_tile_center_y_for_drawing_pawn(self) + newPawnTile.image.get_height()
                for pawn in pawnsSprintTable:
                    if pawn.rect.y == pawnInBettwenY and pawn.rect.x == self.rect.x:
                        return True

    def move_pawn(self, mx, my, chessTilesSprintTable: pygame.sprite.Group, pawnsSprintTable: pygame.sprite.Group,
                 hasdouble_jumped, madeAMove):

        for tileSprite in chessTilesSprintTable:
            if tileSprite.rect.collidepoint((mx, my)):
                if self.check_if_pawn_is_moving_to_the_nearest_tile(tileSprite):
                    if not madeAMove:
                        if tileSprite.check_if_contains_pawn(pawnsSprintTable):
                            self.set_pawn_position(tileSprite.get_tile_center_x_for_drawing_pawn(self),
                                                 tileSprite.get_tile_center_y_for_drawing_pawn(self))
                            return False, True
                        else:
                            return False, False
                    elif hasdouble_jumped:
                        return True, True
                    else:
                        return False, True
                else:
                    if self.check_if_pawn_is_jumping_over(tileSprite):
                        if not hasdouble_jumped:
                            if not madeAMove:
                                if tileSprite.check_if_contains_pawn(pawnsSprintTable):
                                    if self.double_jump(tileSprite, pawnsSprintTable):
                                        self.set_pawn_position(tileSprite.get_tile_center_x_for_drawing_pawn(self),
                                                             tileSprite.get_tile_center_y_for_drawing_pawn(self))
                                        return True, True
                                    else:
                                        return False, False
                                else:
                                    return False, False
                            else:
                                return False, True
                        else:
                            if tileSprite.check_if_contains_pawn(pawnsSprintTable):
                                if self.double_jump(tileSprite, pawnsSprintTable):
                                    self.set_pawn_position(tileSprite.get_tile_center_x_for_drawing_pawn(self),
                                                         tileSprite.get_tile_center_y_for_drawing_pawn(self))
                                    return True, True
                                else:
                                    return True, True
                            else:
                                return True, True
                    else:
                        if madeAMove:
                            return True, True
                        else:
                            return False, False
        if madeAMove:
            if hasdouble_jumped:
                return True, True
            else:
                return False, True
        else:
            return False, False
