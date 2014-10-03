import sys
import pygame
pygame.init()

window = pygame.display.set_mode((640, 480))
ballimg = pygame.image.load("ball.gif")
ballimg2 = pygame.image.load("ball.gif")
ballrect = ballimg.get_rect()

ballrect2 = ballimg2.get_rect()
ballrect2.move([0, 100])

direction = 1
direction2 = 1

variable_clock_frame_skip = 10
physics_clock_frame_skip = 9
clock_count = 0

# input handling (somewhat boilerplate code):
while True:
    clock_count += 1
    if clock_count == variable_clock_frame_skip * physics_clock_frame_skip:
        clock_count = 0

    pygame.time.wait(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

        # print(event)
        # print(pygame.mouse.get_pressed()[0])

    if ballrect[0] + ballrect[2] > 640 or ballrect[0] < 0:
        direction *= -1
    ballrect = ballrect.move([direction*5, 0])
    if ballrect2[0] + ballrect2[2] > 640 or ballrect2[0] < 0:
        direction2 *= -1
    ballrect2 = ballrect2.move([direction2*4, 0])

    window.fill((0, 0, 0))
    window.blit(ballimg, ballrect)
    window.blit(ballimg2, ballrect2)
    pygame.display.flip()
