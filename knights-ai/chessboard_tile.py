import pygame


class ChessBoardTile(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def set_tile_position(self, mx, my):
        self.rect.x = mx
        self.rect.y = my

    def get_tile_center_x(self):
        return int(self.rect.x + self.image.get_width() / 2)

    def get_tile_center_y(self):
        return int(self.rect.y + self.image.get_height() / 2)

    def get_tile_center_x_for_drawing_pawn(self, objectSprite):
        tileX = int(self.rect.x + (self.image.get_width() - objectSprite.image.get_width()) / 2)
        return tileX

    def get_tile_center_y_for_drawing_pawn(self, objectSprite):
        tileY = int(self.rect.y + (self.image.get_height() - objectSprite.image.get_height()) / 2)
        return tileY

    def check_if_contains_pawn(self, pawnsSprintTable: pygame.sprite.Group):
        for pawnSprint in pawnsSprintTable:
            if pawnSprint.rect.collidepoint(
                    (self.get_tile_center_x_for_drawing_pawn(pawnSprint), self.get_tile_center_y_for_drawing_pawn(pawnSprint))):
                return False
        return True

    def check_state(self, pawnsSprintTable: pygame.sprite.Group):
        for pawnSprint in pawnsSprintTable:
            if pawnSprint.rect.collidepoint(
                    (self.get_tile_center_x_for_drawing_pawn(pawnSprint), self.get_tile_center_y_for_drawing_pawn(pawnSprint))):
                if pawnSprint.color == 'white':
                    return 1
                elif pawnSprint.color == 'black':
                    return 2
        return 0
