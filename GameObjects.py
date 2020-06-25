import pygame
import random
BLACK = (0,0,0)
WHITE = (255,255,255)

class Paddle(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image,color,[0,0,width,height])

        self.rect = self.image.get_rect()

    def move(self,pixels):
        self.rect.x += pixels
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 700:
            self.rect.x = 700



class Ball(pygame.sprite.Sprite):
    def __init__(self,color,radius):
        super().__init__()

        self.image = pygame.Surface([radius,radius])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.circle(self.image, color, (radius//2,radius//2) ,radius//2)

        self.velocity = [random.randint(4,8),random.randint(0,8)]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = random.randint(-8, 8)
        self.velocity[1] = random.randint(-8, -4)
    def brick_bounce(self):
        self.velocity[0] = random.randint(-8,8)
        self.velocity[1] = random.randint(-8,8)


class Brick(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image,color,[0,0,width,height])


        self.rect = self.image.get_rect()
