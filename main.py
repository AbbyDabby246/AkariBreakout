import pygame
from GameObjects import Paddle,Ball,Brick

pygame.init()

#colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,89,94)
BLUE = (25,130,196)
YELLOW = (255,202,58)
GREEN = (138,201,38)
PURPLE = (75,0,130)

score = 0
lives = 3

#game window
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Atari Breakout")
icon = pygame.image.load("res/icon.png")
pygame.display.set_icon(icon)

#Paddle
paddle = Paddle(PURPLE,100,13)
paddle.rect.x = 350
paddle.rect.y = 557
pixels = 0

#Ball
ball = Ball(WHITE,17)
ball.rect.x = 395
ball.rect.y = 255

#Sprite list
add_sprites_list = pygame.sprite.Group()
add_sprites_list.add(paddle)
add_sprites_list.add(ball)

#Brick
add_bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick(RED,80,30)
    brick.rect.x = 60 + i*100
    brick.rect.y = 60
    add_sprites_list.add(brick)
    add_bricks.add(brick)
for i in range(7):
    brick = Brick(YELLOW,80,30)
    brick.rect.x = 60 + i*100
    brick.rect.y = 100
    add_sprites_list.add(brick)
    add_bricks.add(brick)
for i in range(7):
    brick = Brick(GREEN,80,30)
    brick.rect.x = 60 + i*100
    brick.rect.y = 140
    add_sprites_list.add(brick)
    add_bricks.add(brick)




#game loop
running = True
clock = pygame.time.Clock()
while running:

    screen.fill(BLUE)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pixels = -5
            if event.key == pygame.K_RIGHT:
                pixels = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pixels = 0



    add_sprites_list.update()

    paddle.move(pixels)

    if ball.rect.x >= 783:
        ball.velocity[0] = -ball.velocity[0]
        ball.rect.x = 783
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
        ball.rect.x = 0
    if ball.rect.y > 580:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            font = pygame.font.Font(None,74)
            text = font.render("GAME OVER",True,WHITE)
            screen.blit(text,(250,300))
            pygame.display.update()
            pygame.time.wait(5000)
            running = False


    if ball.rect.y < 35:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, paddle):
        ball.bounce()

    for brick in pygame.sprite.spritecollide(ball,add_bricks,False):
        ball.brick_bounce()
        score += 1
        brick.kill()
        if len(add_bricks) == 0:
            font = pygame.font.Font(None,74)
            text = font.render("LEVEL COMPLETE",True,WHITE)
            screen.blit(text,(250,300))
            pygame.display.update()
            pygame.time.wait(5000)
            running = False

    #Score and Lives
    font = pygame.font.Font(None,29)
    score_text = font.render("Score :"+str(score),True,WHITE)
    screen.blit(score_text,(10,10))
    lives_text = font.render("Lives :"+str(lives),True,WHITE)
    screen.blit(lives_text,(710,10))
    #Line below text
    pygame.draw.line(screen, WHITE, [0, 35], [800, 35], 2)

    add_sprites_list.draw(screen)
    pygame.display.update()

    clock.tick(60)

pygame.quit()