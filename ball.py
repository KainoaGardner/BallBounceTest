from settings import *
import math
import random
class Ball():
    def __init__(self,x,y,radius,color,mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        # self.xforce = random.randint(-10,10)
        # self.yforce = random.randint(-10,10)
        self.xforce = 0
        self.yforce = 0
        self.force = self.force = math.sqrt(self.xforce ** 2 + self.yforce ** 2)
        self.xVel = 0
        self.yVel = 0
        self.frictionConst = 0.02
        self.frictionForce = 0
        self.xFriction = 0
        self.yFriction = 0
        self.angle = 0
        self.circle = pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)

        self.grabPoint = ()
        # self.releasePoint = ()

    def moveBall(self):
        self.x += self.xVel
        self.y += self.yVel

    def calculateVel(self):
        self.force = math.sqrt(self.xforce ** 2 + self.yforce ** 2)
        self.angle = math.degrees(math.atan2(self.yforce,self.xforce))
        self.frictionForce = self.frictionConst * (self.mass * 9.8)
        self.xFriction = math.cos(math.radians(self.angle)) * self.frictionForce
        self.yFriction = math.sin(math.radians(self.angle)) * self.frictionForce
        self.xforce = math.cos(math.radians(self.angle)) * self.force
        self.xforce = self.xforce - self.xFriction
        self.yforce = math.sin(math.radians(self.angle)) * self.force
        self.yforce = self.yforce - self.yFriction
        self.xVel = self.xforce / self.mass
        self.yVel = self.yforce / self.mass

        if abs(self.xforce) < 0.1:
            self.xforce = 0
        if abs(self.yforce) < 0.1:
            self.yforce = 0

        if abs(self.xVel) < 1:
            self.xVel = 0
        if abs(self.yVel) < 1:
            self.yVel = 0


    def wallCollison(self):
        if (self.x < 0 + self.radius + wallThickness / 2 and self.xVel < 0) or (self.x > WIDTH - self.radius - wallThickness / 2 and self.xVel > 0):
            self.xforce *= -1

        if (self.y < 0 + self.radius + wallThickness / 2 and self.yVel < 0) or (self.y > HEIGHT - self.radius - wallThickness / 2 and self.yVel > 0):
            self.yforce *= -1

    def ballCollide(self,ball):
        xDif = self.x - ball.x
        yDif = self.y - ball.y
        distance = math.sqrt(xDif ** 2 + yDif ** 2)
        if distance < ball.radius + self.radius:
            ball.x = self.x - xDif * 1.1
            ball.y = self.y - yDif * 1.1
            xtempForce = ball.xforce
            ytempForce = ball.yforce

            ball.xforce = self.xforce
            ball.yforce = self.yforce
            self.xforce = xtempForce
            self.yforce = ytempForce

            print(("self",self.mass,self.xforce,self.yforce,self.xVel,self.yVel))
            print(("ball",ball.mass,ball.xforce,ball.yforce,ball.xVel,ball.yVel))



    def shootBall(self,releasePoint):
        if self.grabPoint != ():
            self.grabPoint = ()
            xDif = releasePoint[0] - self.x
            yDif = releasePoint[1] - self.y

            self.xforce = xDif / 100
            self.yforce = yDif / 100

    def displayArrow(self):
        if self.grabPoint != ():
            pygame.draw.line(screen,self.color,(self.x,self.y),pygame.mouse.get_pos(),self.radius // 2)

    def display(self):
        self.circle = pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)

    def checkClicked(self,pos):
        if self.x - self.radius <= pos[0] <= self.x + self.radius and self.y - self.radius <= pos[1] <= self.y + self.radius:
            self.grabPoint = pos

    def update(self):
        self.calculateVel()
        # print((self.force, self.xforce, self.yforce))
        # print((self.xVel,self.yVel))
        self.displayArrow()
        self.moveBall()
        self.wallCollison()
        self.display()




ball1 = Ball(random.randint(0 + 25 + wallThickness // 2, WIDTH - 25 - wallThickness // 2),random.randint(0 + 25 + wallThickness // 2, HEIGHT - 25 - wallThickness // 2),25,"#e74c3c",0.100)
ball2 = Ball(random.randint(0 + 35 + wallThickness // 2, WIDTH - 35 - wallThickness // 2),random.randint(0 + 35 + wallThickness // 2, HEIGHT - 35 - wallThickness // 2),35,"#3498db",0.200)
ball3 = Ball(random.randint(0 + 45 + wallThickness // 2, WIDTH - 45 - wallThickness // 2),random.randint(0 + 45 + wallThickness // 2, HEIGHT - 45 - wallThickness // 2),45,"#27ae60",0.300)

ballGroup = [ball1,ball2,ball3]
# ballGroup.append(ball1)