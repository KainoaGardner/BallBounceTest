from display import *

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for ball in ballGroup:
                        ball.checkClicked(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    for ball in ballGroup:
                        if ball.grabPoint != ():
                            ball.shootBall(pygame.mouse.get_pos())
        display()
    pygame.quit()

main()