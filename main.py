import pygame

# initialize pygame
pygame.init()
# creating the title and icon
pygame.display.set_caption("Alien Invasion!!!")
icon = pygame.image.load("images/rocket.png")
pygame.display.set_icon(icon)
# Player
playerImg = pygame.image.load("images/spaceship.png")
# x-coordinate of the player
playerX = 370
# y-coordinate of the player
playerY = 480
# function to draw the player on the screen
def player():
    screen.blit(playerImg, (playerX, playerY))
# creating the screen
screen = pygame.display.set_mode((800, 600))
# loop
running = True
while running == True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            screen.fill((0, 0, 0))
player()
pygame.display.update ()