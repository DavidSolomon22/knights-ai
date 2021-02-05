import pygame
import game
import game_with_ai

pygame.init()

screen = pygame.display.set_mode((800, 600))
gameIcon = pygame.image.load('resources/game_icon.jpg')
menuBackground = pygame.image.load('resources/menu_background.jpg')
menuBackground = pygame.transform.scale(menuBackground, (800, 600))
blackColor = (0, 0, 0)

pygame.display.set_caption("Knights AI")
pygame.display.set_icon(gameIcon)


def draw_text(text, font, fontSize, color, surface, x, y):
    messageText = pygame.font.Font(f'resources/{font}', fontSize)
    textObj = messageText.render(text, 1, color)
    textRect = textObj.get_rect()
    textRect.topleft = (x, y)
    surface.blit(textObj, textRect)
    return textRect


click = False

def main_menu():
    while True:

        screen.fill((0, 0, 0))
        screen.blit(menuBackground, (0, 0))
        gameName = draw_text('KNIGHTS', 'game_title_font.ttf', 80, blackColor, screen, 50, 50)
        menuPlay = draw_text('Play', 'menu_font.otf', 45, blackColor, screen, 80, 220)
        menuPlayWithAI = draw_text('Play With AI', 'menu_font.otf', 45, blackColor, screen, 80, 340)
        menuExit = draw_text('Exit', 'menu_font.otf', 45, blackColor, screen, 80, 460)

        mx, my = pygame.mouse.get_pos()

        if menuPlay.collidepoint((mx, my)):
            if click:
                game.draw_chess_board_with_pawns(800, 600, screen)
        if menuPlayWithAI.collidepoint((mx, my)):
            if click:
                game_with_ai.draw_chess_board_with_pawns(800, 600, screen)
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


main_menu()
