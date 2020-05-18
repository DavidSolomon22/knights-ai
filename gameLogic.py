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


class Pawn(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        if image == "white":
            self.image = pygame.image.load('Resources/whitePawn.png')
        else:
            self.image = pygame.image.load('Resources/blackPawn.png')

        self.rect = self.image.get_rect()

    def setPawnPosition(self, mx, my):
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
                tile = ChessBoardTile(whiteTile, tileSize, tileSize)
                tile.setTilePosition((y * tileSize + (width - height) / 2), (x * tileSize))
                spriteList.add(tile)
                tileColorIndex = (tileColorIndex + 1) % 2
            else:
                tile = ChessBoardTile(darkTile, tileSize, tileSize)
                tile.setTilePosition((y * tileSize + (width - height) / 2), (x * tileSize))
                spriteList.add(tile)
                tileColorIndex = (tileColorIndex + 1) % 2

    return spriteList


def drawChessBoardWithPawns(x, y, screen: pygame.Surface):
    pygame.init()

    screenWidth = x
    screenHeight = y

    # screen = pygame.display.set_mode((screenWidth, screenHeight))

    screen.fill((0, 0, 0))

    chessTilesGroup = pygame.sprite.Group()

    chessPawnsGroup = pygame.sprite.Group()

    chessTilesCreatedTable = drawChessboard(x, y, chessTilesGroup)

    chessTilesCreatedTable.draw(screen)

    for index, tile in enumerate(chessTilesCreatedTable):
        rectangleCenterX = tile.rect.x / 2
        rectangleCenterY = tile.rect.y / 2
        tileSize = tile.image.get_width()
        if index <= 15:
            pawn = Pawn('white')
            chessPawnsGroup.add(pawn)
            pawn.setPawnPosition(tile.rect.x + (tileSize - pawn.image.get_width())/2, tile.rect.y + (tileSize - pawn.image.get_width())/2)
        elif index >= 48:
            pawn = Pawn('black')
            chessPawnsGroup.add(pawn)
            pawn.setPawnPosition(tile.rect.x + (tileSize - pawn.image.get_width())/2, tile.rect.y + (tileSize - pawn.image.get_width())/2)

    chessPawnsGroup.draw(screen)

    gameRunning = True
    while gameRunning:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        pygame.display.update()
