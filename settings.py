import pygame

pygame.init()
TILESIZE = 100
WIDTH = TILESIZE * 10
HEIGHT = TILESIZE * 10
FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("BallCollideGameTest")
clock = pygame.time.Clock()

boardImage = pygame.image.load("graphics/bg.jpg").convert()
boardImage = pygame.transform.scale(boardImage,(WIDTH,HEIGHT))

brown = "#6F4E37"
wallThickness = 50