import pygame


class Menu():
    def __init__(self, window: pygame.Surface):
        self.gameWindow = window
        self.menuBackground = pygame.image.load('Resources/menuBackground.jpg')
        self.menuBackground = pygame.transform.scale(self.menuBackground, (800, 600))
        self.black=(0,0,0)

    def textObjects(self,message, font: pygame.font):
        textSurface = font.render(message, font, self.black)
        return textSurface, textSurface.get_rect()

    def displayMenuOption(self, message,x,y):
        messageText = pygame.font.Font('Resources/menuFont.otf', 45)
        textToRender = messageText.render(message, True, self.black)
        textRectangle = textToRender.get_rect()
        textRectangle.center = (x,y)
        self.gameWindow.blit(textToRender, textRectangle)

    def drawMenu(self):
        self.gameWindow.fill((0, 0, 0))
        self.gameWindow.blit(self.menuBackground, (0, 0))
        self.displayMenuOption("Play",100,220)
        self.displayMenuOption("Exit",100,340)

    def hoverOverMenuButton(self, mousePos):
        if

