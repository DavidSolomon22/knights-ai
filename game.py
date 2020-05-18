import pygame


class Pawn:

    def __init__(self, image, target_pos):
        self.image = image
        self.target_pos = target_pos
        self.pos = target_pos


    def update(self):
        return

    def draw(self, target_surf):
        target_surf.blit(self.image, self.pos)

    def contains(self, pt):
        (posx, posy) = self.pos
        pawn_width = self.image.get_width()
        pawn_height = self.image.get_height()
        (x, y) = pt
        return (x >= posx and x < posx + pawn_width and y >= posy and y < posy + pawn_height)

    def move(self, pos):
        self.pos = pos


def showPossibleMove(sprite):
    pos = list(sprite.pos)
    pos[0] = 262


def drawChessBoard():
    whitePawnsLine1 = [6, 6, 6, 6, 6, 6, 6, 6]
    whitePawnsLine2 = [7, 7, 7, 7, 7, 7, 7, 7]
    blackPawnsLine1 = [0, 0, 0, 0, 0, 0, 0, 0]
    blackPawnsLine2 = [1, 1, 1, 1, 1, 1, 1, 1]


    actual_positon = (0, 0)
    actual_sprite = Pawn('', 0)

    spritesTable = []
    rowSize = 8
    surface_size = 800
    squareSize = surface_size // rowSize
    chessboard = pygame.display.set_mode((surface_size, surface_size))
    colors = [(205, 133, 63), (255, 235, 205)]

    white_pawn = pygame.image.load("Resources/pawn.png")
    white_pawn_center = (squareSize - white_pawn.get_width()) // 2

    black_pawn = pygame.image.load("Resources/black1.png")
    black_pawn_center = (squareSize - black_pawn.get_width()) // 2

    for (x, y) in enumerate(whitePawnsLine1):
        pawnSprite = Pawn(white_pawn, ((x * squareSize + white_pawn_center), y * squareSize + white_pawn_center))
        spritesTable.append(pawnSprite)

    for (x, y) in enumerate(whitePawnsLine2):
        pawnSprite2 = Pawn(white_pawn, ((x * squareSize + white_pawn_center), y * squareSize + white_pawn_center))
        spritesTable.append(pawnSprite2)

    for (x, y) in enumerate(blackPawnsLine1):
        pawnSprite3 = Pawn(black_pawn, (x * squareSize + black_pawn_center, y * squareSize + black_pawn_center))
        spritesTable.append(pawnSprite3)

    for (x, y) in enumerate(blackPawnsLine2):
        pawnSprite4 = Pawn(black_pawn, (x * squareSize + black_pawn_center, y * squareSize + black_pawn_center))
        spritesTable.append(pawnSprite4)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.dict["pos"]
            actual_positon = pos
            print(pos)

        if event.type == pygame.MOUSEBUTTONUP:
            print('up' + str(actual_sprite))
            if (actual_sprite.pos != 0):
                print(actual_sprite.pos)
                cord = list(actual_sprite.pos)
                cordx = cord[0]
                cordy = cord[1]
                for sprite in spritesTable:
                    if (sprite.contains((cordx - 60, cordy))):
                        print(' pionek po lewej')
                    if (sprite.contains((cordx + 60, cordy))):
                        print(' pionek po prawej')
                    if (sprite.contains((cordx, cordy + 60))):
                        print('pionek na dole')
                    if (sprite.contains((cordx, cordy - 60))):
                        print('pionek na gorze')

        for sprite in spritesTable:
            if (sprite.contains(actual_positon)):
                actual_sprite = sprite
                break

        for x in range(rowSize):
            c_index = x % 2
            for y in range(rowSize):
                rect = (y * squareSize, x * squareSize, squareSize, squareSize)
                chessboard.fill(colors[c_index], rect)
                c_index = (c_index + 1) % 2

        for sprite in spritesTable:
            sprite.update()

        for sprite in spritesTable:
            sprite.draw(chessboard)


        pygame.display.update()

    pygame.quit()
