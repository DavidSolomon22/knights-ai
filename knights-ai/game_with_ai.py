import pygame
import pawn
import chessboard_tile
import time
import mcts

def create_chessboard(width, height):
    whiteTileColor = (232, 235, 239)
    darkTileColor = (125, 135, 150)

    spriteList = pygame.sprite.Group()

    tileSize = height / 8

    for x in range(8):
        tileColorIndex = x % 2
        for y in range(8):
            if tileColorIndex == 0:
                tile = chessboard_tile.ChessBoardTile(whiteTileColor, tileSize, tileSize)
                tile.set_tile_position((y * tileSize + (width - height) / 2), (x * tileSize))
                spriteList.add(tile)
                tileColorIndex = (tileColorIndex + 1) % 2
            else:
                tile = chessboard_tile.ChessBoardTile(darkTileColor, tileSize, tileSize)
                tile.set_tile_position((y * tileSize + (width - height) / 2), (x * tileSize))
                spriteList.add(tile)
                tileColorIndex = (tileColorIndex + 1) % 2

    return spriteList


def create_pawns_on_chessboard(chessTilesSprintTable: pygame.sprite.Group):
    pawnsSprintTable = pygame.sprite.Group()

    for index, tile in enumerate(chessTilesSprintTable):
        tileSize = tile.image.get_width()
        if index <= 15:
            pawn_var = pawn.Pawn('black')
            pawnsSprintTable.add(pawn_var)
            pawn_var.set_pawn_position(tile.rect.x + (tileSize - pawn_var.image.get_width()) / 2,
                                 tile.rect.y + (tileSize - pawn_var.image.get_width()) / 2)
        elif index >= 48:
            pawn_var = pawn.Pawn('white')
            pawnsSprintTable.add(pawn_var)
            pawn_var.set_pawn_position(tile.rect.x + (tileSize - pawn_var.image.get_width()) / 2,
                                 tile.rect.y + (tileSize - pawn_var.image.get_width()) / 2)

    return pawnsSprintTable


def draw_text(text, font, fontSize, color, surface, x, y):
    messageText = pygame.font.Font(f'resources/{font}', fontSize)
    textobj = messageText.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    return textrect


def display_player_name(roundIndex, screen: pygame.Surface):
    if roundIndex % 2 == 0:
        playerText1 = draw_text('Player 1', 'game_title_font.ttf', 20, (255, 255, 255), screen, 0, 560)
        return playerText1
    elif roundIndex % 2 == 1:
        playerText2 = draw_text('Player 2', 'game_title_font.ttf', 20, (255, 255, 255), screen, 0, 0)
        return playerText2

def move_player_with_ai(pawnsSprintTable: pygame.sprite.Group,chessTilesSprintTable: pygame.sprite.Group, action):
    pawnX = chessTilesSprintTable.sprites()[action[0]].get_tile_center_x_for_drawing_pawn(pawnsSprintTable.sprites()[0])
    pawnY = chessTilesSprintTable.sprites()[action[0]].get_tile_center_y_for_drawing_pawn(pawnsSprintTable.sprites()[0])

    pawn_X_to_move = chessTilesSprintTable.sprites()[action[1]].get_tile_center_x_for_drawing_pawn(pawnsSprintTable.sprites()[0])
    pawn_Y_to_move = chessTilesSprintTable.sprites()[action[1]].get_tile_center_y_for_drawing_pawn(pawnsSprintTable.sprites()[0])

    pawn_to_move = [pawn for pawn in pawnsSprintTable if (pawn.rect.x == pawnX) and (pawn.rect.y == pawnY)]

    if len(pawn_to_move) != 0:
        pawn_to_move[0].set_pawn_position(pawn_X_to_move,pawn_Y_to_move)


def draw_chess_board_with_pawns(screenWidth, screenHeight, screen: pygame.Surface):
    pygame.init()

    UCT = mcts.UCTWins()

    chessTilesSprintTable = create_chessboard(screenWidth, screenHeight)

    pawnsSprintTable = create_pawns_on_chessboard(chessTilesSprintTable)

    gameRunning = True

    click = False

    chosenPawn = False
    clickedPawn: pawn

    hasdouble_jumped = False
    madeAMove = False

    roundIndex = 0

    whitePawnAtEnd = []
    blackPawnAtEnd = []

    while gameRunning:

        screen.fill((0, 0, 0))

        finishButton = draw_text('End turn', 'game_title_font.ttf', 17, (255, 255, 255), screen, 710, 300)

        mx, my = pygame.mouse.get_pos()

        if roundIndex % 2 == 1:
            action = UCT.get_action(chessTilesSprintTable,pawnsSprintTable,roundIndex)
            move_player_with_ai(pawnsSprintTable, chessTilesSprintTable, action)
            roundIndex += 1

        for pawnSprite in pawnsSprintTable:
            if pawnSprite.rect.collidepoint((mx, my)):
                if click:
                    if roundIndex % 2 == 0:
                        if pawnSprite.color == 'white':
                            chosenPawn = True
                            clickedPawn = pawnSprite
                            clickedPawn.pawn_selected()

        display_player_name(roundIndex, screen)

        if click:
            if finishButton.collidepoint((mx, my)):
                if madeAMove:
                    if clickedPawn != None:
                        clickedPawn.pawn_unselected()
                    hasdouble_jumped = False
                    madeAMove = False
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
                        hasdouble_jumped, madeAMove = clickedPawn.move_pawn(mx, my, chessTilesSprintTable,
                                                                          pawnsSprintTable, hasdouble_jumped, madeAMove)
                        clickedPawn.pawn_unselected()
                        chosenPawn = False
                        clickedPawn = None
                        click = False
                elif event.button == 3:
                    chosenPawn = False
                    if clickedPawn != None:
                        clickedPawn.pawn_unselected()
                    clickedPawn = None
                    click = False

        for sprite in pawnsSprintTable:
            if sprite.color == 'white':
                if len(whitePawnAtEnd) == 16:
                    screen.fill((0,0,0))
                    playerWin = draw_text('Player 1 Wins', 'gameTitleFont.ttf', 50, (255, 180, 0), screen, 240, 240)
                    pygame.display.update()
                    time.sleep(0.2)
                    gameRunning = False
                if sprite in whitePawnAtEnd:
                    if sprite.rect.y > 96:
                        whitePawnAtEnd.remove(sprite)
                else:
                    if sprite.rect.y <= 96:
                        whitePawnAtEnd.append(sprite)
            else:
                if len(blackPawnAtEnd) == 16:
                    screen.fill((0, 0, 0))
                    playerWin2 = draw_text('Player 2 Wins', 'gameTitleFont.ttf', 50, (255, 180, 0), screen, 240, 240)
                    pygame.display.update()
                    time.sleep(0.2)
                    gameRunning = False
                if sprite in blackPawnAtEnd:
                    if sprite.rect.y < 471:
                        blackPawnAtEnd.remove(sprite)
                else:
                    if sprite.rect.y >= 471:
                        blackPawnAtEnd.append(sprite)

        chessTilesSprintTable.draw(screen)

        pawnsSprintTable.draw(screen)

        pygame.display.update()
