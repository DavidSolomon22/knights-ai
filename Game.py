import pygame
import Pawn
import ChessBoardTile


def drawChessboard(width, height, screen: pygame.Surface):
    whiteTileColor = (232, 235, 239)
    darkTileColor = (125, 135, 150)

    spriteList = pygame.sprite.Group()

    tileSize = height / 8

    for x in range(8):
        tileColorIndex = x % 2
        for y in range(8):
            if tileColorIndex == 0:
                tile = ChessBoardTile.ChessBoardTile(whiteTileColor, tileSize, tileSize)
                tile.setTilePosition((y * tileSize + (width - height) / 2), (x * tileSize))
                spriteList.add(tile)
                tileColorIndex = (tileColorIndex + 1) % 2
            else:
                tile = ChessBoardTile.ChessBoardTile(darkTileColor, tileSize, tileSize)
                tile.setTilePosition((y * tileSize + (width - height) / 2), (x * tileSize))
                spriteList.add(tile)
                tileColorIndex = (tileColorIndex + 1) % 2

    spriteList.draw(screen)

    return spriteList


def drawPawnsOnChessboard(chessTilesSprintTable: pygame.sprite.Group, screen: pygame.Surface):
    pawnsSprintTable = pygame.sprite.Group()

    for index, tile in enumerate(chessTilesSprintTable):
        tileSize = tile.image.get_width()
        if index <= 15:
            pawn = Pawn.Pawn('white')
            pawnsSprintTable.add(pawn)
            pawn.setPawnPosition(tile.rect.x + (tileSize - pawn.image.get_width()) / 2,
                                 tile.rect.y + (tileSize - pawn.image.get_width()) / 2)
        elif index >= 48:
            pawn = Pawn.Pawn('black')
            pawnsSprintTable.add(pawn)
            pawn.setPawnPosition(tile.rect.x + (tileSize - pawn.image.get_width()) / 2,
                                 tile.rect.y + (tileSize - pawn.image.get_width()) / 2)

    pawnsSprintTable.draw(screen)

    return pawnsSprintTable


def drawChessBoardWithPawns(screenWidth, screenHeight, screen: pygame.Surface):
    pygame.init()
    screen.fill((0, 0, 0))

    chessTilesSprintTable = drawChessboard(screenWidth, screenHeight, screen)

    pawnsSprintTable = drawPawnsOnChessboard(chessTilesSprintTable, screen)

    gameRunning = True

    while gameRunning:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameRunning = False

        pygame.display.update()
