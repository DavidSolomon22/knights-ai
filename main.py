import pygame
import menu

pygame.init()

screen = pygame.display.set_mode((800, 600))
gameIcon = pygame.image.load('Resources/gameIcon.jpg')

pygame.display.set_caption("Knights AI")
pygame.display.set_icon(gameIcon)

# initialize game menu
gameMenu = menu.Menu(screen)

gameLoop = True

while gameLoop:
    gameMenu.drawMenu()

    for event in pygame.event.get():
        mousePosition = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()
            gameLoop = False

    pygame.display.update()
