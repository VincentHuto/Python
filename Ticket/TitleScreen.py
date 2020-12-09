import pygame
import sys

pygame.init()

##sets the window size to 800x600px
display_width = 1024
display_height = 512

##easy access to colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):  # x=362 y=100 w = 200 h =75
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "play":
                gameLoop()
            elif action == "quite":
                pygame.quit()
                quit()

    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = (x + (w / 2), (y + (h / 2)))
    screen.blit(textSurf, textRect)


# Allows the background image to be loaded with a method background needs to be atleast the size of the window
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


##makes the screen as wide and tall as above variables, makes a white background, adds TTR title, and starts a clock
screen = pygame.display.set_mode([display_width, display_height])
screen.fill(white)
pygame.display.set_caption("TTR")
clock = pygame.time.Clock()
BackGround = Background('Ticket To Ride Assets\BackGrounds\Background.png', [0, 0])
screen.blit(BackGround.image, BackGround.rect)

##main while loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

    # x=362 y=100 w = 200 h =75
    button("start Train-ing", 362, 100, 200, 75, red, green, "play")
    button("Coward", 362, 200, 200, 75, green, red, "quit")




    pygame.display.update()
    clock.tick(10)

pygame.quit()
quit()
