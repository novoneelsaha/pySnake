import pygame

# initialize pygame
pygame.init()
# creating the title and icon
pygame.display.set_caption("Alien Invasion!!!")
icon = pygame.image.load("rocket.png")
pygame.display.set_icon(icon)
# creating the screen
screen = pygame.display.set_mode((800, 600))
# loop
running = True
while running == True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False