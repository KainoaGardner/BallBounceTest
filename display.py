from settings import *
from ball import *
def display():
    screen.blit(boardImage,(0,0))
    drawWall()
    for ball in ballGroup:
        ball.update()

    # for ball in ballGroup:
    #     ball.ballCollide(ball2)
    #     ball.ballCollide(ball3)

    pygame.display.update()
    clock.tick(FPS)

def drawWall():
    leftWall = pygame.draw.line(screen,brown,(0,0),(0,HEIGHT),wallThickness)
    rightWall = pygame.draw.line(screen, brown, (WIDTH, 0), (WIDTH, HEIGHT), wallThickness)
    topWall = pygame.draw.line(screen, brown, (0, 0), (WIDTH, 0), wallThickness)
    botWall = pygame.draw.line(screen, brown, (0, HEIGHT), (WIDTH, HEIGHT), wallThickness)