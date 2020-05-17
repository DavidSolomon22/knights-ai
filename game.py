import pygame



class Pawn:

    def __init__(self, image, target_pos):
        self.image = image
        self.target_pos = target_pos
        self.pos = target_pos
        # (x,y)=target_pos
        # self.pos=(x,0)
        # self.y_velo=0

    def update(self):
        return
        # self.y_velo += grav
        # (x,y)=self.pos
        # new_pos_y=y+self.y_velo
        # self.pos=(x,new_pos_y)

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
    pos=list(sprite.pos)
    pos[0]=262



def drawChessBoard():
    whity = [6, 6, 6, 6, 6, 6, 6, 6]
    whity2 = [7, 7, 7, 7, 7, 7, 7, 7]
    blacks = [0, 0, 0, 0, 0, 0, 0, 0]
    blacks2 = [1, 1, 1, 1, 1, 1, 1, 1]
    pygame.init()

    actual_positon=(0,0)
    actual_sprite=Pawn('',0)
    ticks=0
    sprites=[]
    size=8
    surface_size=480
    sq=surface_size //size
    chessboard=pygame.display.set_mode((surface_size,surface_size))
    colors = [(205, 133, 63), (255, 235, 205)]

    white_pawn = pygame.image.load("Resources/pawn.png")
    white_pawn_center = (sq - white_pawn.get_width()) // 2

    black_pawn = pygame.image.load("Resources/black1.png")
    black_pawn_center = (sq - black_pawn.get_width()) // 2

    for (x, y) in enumerate(whity):
        pawnSprite = Pawn(white_pawn, ((x * sq + white_pawn_center), y * sq + white_pawn_center))
        sprites.append(pawnSprite)

    for (x, y) in enumerate(whity2):
        pawnSprite2 = Pawn(white_pawn, ((x * sq + white_pawn_center), y * sq + white_pawn_center))
        sprites.append(pawnSprite2)

    for (x, y) in enumerate(blacks):
        pawnSprite3 = Pawn(black_pawn, (x * sq + black_pawn_center, y * sq + black_pawn_center))
        sprites.append(pawnSprite3)

    for (x, y) in enumerate(blacks2):
        pawnSprite4 = Pawn(black_pawn, (x * sq + black_pawn_center, y * sq + black_pawn_center))
        sprites.append(pawnSprite4)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos=event.dict["pos"]
            actual_positon=pos
            print(pos)


        if event.type == pygame.MOUSEBUTTONUP:
            print('up'+str(actual_sprite))
            #actual_sprite.move(actual_positon)
            if(actual_sprite.pos!=0):
                print(actual_sprite.pos)
                cord=list(actual_sprite.pos)
                cordx=cord[0]
                cordy=cord[1]
                for sprite in sprites:
                    if(sprite.contains((cordx-60,cordy))):
                        print(' pionek po lewej')
                    if(sprite.contains((cordx+60,cordy))):
                        print(' pionek po prawej')
                    if (sprite.contains((cordx,cordy+60))):
                        print('pionek na dole')
                    if (sprite.contains((cordx, cordy-60))):
                        print('pionek na gorze')



        for sprite in sprites:
            if (sprite.contains(actual_positon)):
                actual_sprite = sprite
                #print('touch'+str(actual_sprite))
                break



        for x in range(size):
            c_index = x % 2
            for y in range(size):
                rect = (y * sq, x * sq, sq, sq)
                chessboard.fill(colors[c_index], rect)
                c_index = (c_index + 1) % 2

        for sprite in sprites:
            sprite.update()

        for sprite in sprites:
            sprite.draw(chessboard)

        # for (x,y) in enumerate(whity):
        #     chessboard.blit(white_pawn, ((x * sq + white_pawn_center), y * sq + white_pawn_center))
        #
        # for (x, y) in enumerate(whity2):
        #     chessboard.blit(white_pawn, ((x * sq + white_pawn_center), y * sq + white_pawn_center))
        #
        # for(x,y) in enumerate(blacks):
        #     chessboard.blit(black_pawn,(x*sq+black_pawn_center,y*sq+black_pawn_center))
        #
        # for (x, y) in enumerate(blacks2):
        #     chessboard.blit(black_pawn, (x * sq + black_pawn_center, y * sq + black_pawn_center))

        pygame.display.flip()

    pygame.quit()
