import pygame


class chessBoardTile(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)


        # rectangle to detect collisions
        self.rect = self.image.get_rect()

    def setTilePosition(self, mx, my):
        self.rect.x = mx
        self.rect.y = my


def drawChessboard(width, height, spriteList: pygame.sprite.Group):
    whiteTile = (232, 235, 239)
    darkTile = (125, 135, 150)

    tileSize = height / 8

    for x in range(8):
        tileColorIndex = x % 2
        for y in range(8):
            if tileColorIndex == 0:
                tile = chessBoardTile(whiteTile, tileSize, tileSize)
                tile.setTilePosition((y * tileSize + (width - height)/2), (x * tileSize))
                spriteList.add(tile)
                tileColorIndex = (tileColorIndex + 1) % 2
            else:
                tile = chessBoardTile(darkTile, tileSize, tileSize)
                tile.setTilePosition((y * tileSize + (width - height)/2), (x * tileSize))
                spriteList.add(tile)
                tileColorIndex = (tileColorIndex + 1) % 2

    return spriteList


def drawChessBoardWithPawns(x, y):
    screenWidth = x
    screenHeight = y

    screen = pygame.display.set_mode((screenWidth, screenHeight))

    screen.fill((0, 0, 0))

    chessTilesGroup = pygame.sprite.Group()

    chessTilesCreated = drawChessboard(x, y, chessTilesGroup)

    chessTilesCreated.draw(screen)

    gameRunning = True
    while gameRunning:


        pygame.display.update()
