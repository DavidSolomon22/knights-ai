import pygame
import game

pygame.init()

screen = pygame.display.set_mode((800, 600))
gameIcon = pygame.image.load('Resources/gameIcon.jpg')
menuBackground = pygame.image.load('Resources/menuBackground.jpg')
menuBackground = pygame.transform.scale(menuBackground, (800, 600))
blackColor = (0, 0, 0)

pygame.display.set_caption("Knights AI")
pygame.display.set_icon(gameIcon)


def draw_text(text, font, fontSize , color, surface, x, y):
    messageText = pygame.font.Font(f'Resources/{font}', fontSize)
    textobj = messageText.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    return textrect


click = False


def main_menu():
    while True:

        screen.fill((0, 0, 0))
        screen.blit(menuBackground, (0, 0))
        gameName = draw_text('KNIGHTS', 'gameTitleFont.ttf',80, blackColor, screen, 50,50)
        menuPlay = draw_text('Play','menuFont.otf',45, blackColor, screen, 100, 220)
        menuExit = draw_text('Exit','menuFont.otf',45,blackColor, screen, 100, 340)

        mx, my = pygame.mouse.get_pos()

        if menuPlay.collidepoint((mx, my)):
            if click:
                game.drawChessBoard()
        if menuExit.collidepoint((mx, my)):
            if click:
                pygame.quit()

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()



# def options():
#     running = True
#     while running:
#         screen.fill((0, 0, 0))
#
#         # draw_text('options', font, (255, 255, 255), screen, 20, 20)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     running = False
#
#         pygame.display.update()


main_menu()
