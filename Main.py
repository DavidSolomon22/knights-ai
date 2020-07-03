import pygame
import Game
import mcts
import GameWithAI

pygame.init()

screen = pygame.display.set_mode((800, 600))
gameIcon = pygame.image.load('Resources/gameIcon.jpg')
menuBackground = pygame.image.load('Resources/menuBackground.jpg')
menuBackground = pygame.transform.scale(menuBackground, (800, 600))
blackColor = (0, 0, 0)

pygame.display.set_caption("Knights AI")
pygame.display.set_icon(gameIcon)


def draw_text(text, font, fontSize, color, surface, x, y):
    messageText = pygame.font.Font(f'Resources/{font}', fontSize)
    textObj = messageText.render(text, 1, color)
    textRect = textObj.get_rect()
    textRect.topleft = (x, y)
    surface.blit(textObj, textRect)
    return textRect


click = False

# uct = mcts.UCTWins('tutaj przekazac obiekt ten z poczatkowym stanem gry w pygame, ktory mamy przelozyc na tablice 1d')


def main_menu():
    while True:

        screen.fill((0, 0, 0))
        screen.blit(menuBackground, (0, 0))
        gameName = draw_text('KNIGHTS', 'gameTitleFont.ttf', 80, blackColor, screen, 50, 50)
        menuPlay = draw_text('Play', 'menuFont.otf', 45, blackColor, screen, 80, 220)
        menuPlayWithAI = draw_text('Play With AI', 'menuFont.otf', 45, blackColor, screen, 80, 340)
        menuExit = draw_text('Exit', 'menuFont.otf', 45, blackColor, screen, 80, 460)

        mx, my = pygame.mouse.get_pos()

        if menuPlay.collidepoint((mx, my)):
            if click:
                Game.drawChessBoardWithPawns(800, 600, screen)
        if menuPlayWithAI.collidepoint((mx, my)):
            if click:
                GameWithAI.drawChessBoardWithPawns(800, 600, screen)
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
