import pygame
import Pawn
import ChessBoardTile


def createChessboard(width, height):
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

    return spriteList


def createPawnsOnChessboard(chessTilesSprintTable: pygame.sprite.Group):
    pawnsSprintTable = pygame.sprite.Group()

    for index, tile in enumerate(chessTilesSprintTable):
        tileSize = tile.image.get_width()
        if index <= 15:
            pawn = Pawn.Pawn('black')
            pawnsSprintTable.add(pawn)
            pawn.setPawnPosition(tile.rect.x + (tileSize - pawn.image.get_width()) / 2,
                                 tile.rect.y + (tileSize - pawn.image.get_width()) / 2)
        elif index >= 48:
            pawn = Pawn.Pawn('white')
            pawnsSprintTable.add(pawn)
            pawn.setPawnPosition(tile.rect.x + (tileSize - pawn.image.get_width()) / 2,
                                 tile.rect.y + (tileSize - pawn.image.get_width()) / 2)

    return pawnsSprintTable

def draw_text(text, font, fontSize , color, surface, x, y):
    messageText = pygame.font.Font(f'Resources/{font}', fontSize)
    textobj = messageText.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    return textrect


def drawChessBoardWithPawns(screenWidth, screenHeight, screen: pygame.Surface):
    pygame.init()
    screen.fill((0, 0, 0))

    chessTilesSprintTable = createChessboard(screenWidth, screenHeight)

    pawnsSprintTable = createPawnsOnChessboard(chessTilesSprintTable)

    gameRunning = True

    click = False

    chosenPawn = False

    clickedPawn: Pawn
    player=1


    roundIndex = 0

    while gameRunning:

        screen.fill((0, 0, 0))

        if (player == 1):
            playerText = draw_text('Player 1', 'gameTitleFont.ttf', 20, (255, 255, 255), screen, 0, 560)
        elif (player == 2):
            player2Text = draw_text('Player 2', 'gameTitleFont.ttf', 20, (255, 255, 255), screen, 0, 0)

        mx, my = pygame.mouse.get_pos()

        for pawnSprite in pawnsSprintTable:
            if pawnSprite.rect.collidepoint((mx, my)):
                if click:
                    if roundIndex % 2 == 0:
                        if pawnSprite.color == 'white':
                            chosenPawn = True
                            clickedPawn = pawnSprite
                            clickedPawn.PawnSelected()
                            roundIndex += 1
                    else:
                        if pawnSprite.color == 'black':
                            chosenPawn = True
                            clickedPawn = pawnSprite
                            clickedPawn.PawnSelected()
                            roundIndex += 1

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    if click and chosenPawn:
                        if clickedPawn.movePawn(mx, my, chessTilesSprintTable, pawnsSprintTable):
                            if (clickedPawn.color == 'white'):
                                player = 2
                            else:
                                player = 1
                            clickedPawn.PawnUnselected()
                            chosenPawn = False
                            clickedPawn = None
                            click = False
                        else:
                            clickedPawn.PawnUnselected()
                            chosenPawn = False
                            clickedPawn = None
                            click = False
                            roundIndex -= 1
                elif event.button == 3:
                    chosenPawn = False
                    clickedPawn.PawnUnselected()
                    clickedPawn = None
                    click = False
                    roundIndex -= 1

        chessTilesSprintTable.draw(screen)



        pawnsSprintTable.draw(screen)




        pygame.display.update()

