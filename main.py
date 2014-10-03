import sys
import pygame


def top_left_coord_of_object_where_mid_is(text_object_size, mid_coords):
    return (mid_coords[0] - (text_object_size[0]/2),
            mid_coords[1] - (text_object_size[1]/2))


def middle_coords_of_text(text_object):
    pass


def is_within(coords, rect):
    if (coords[0] >= rect[0] and
            coords[0] <= rect[0] + rect[2] and
            coords[1] >= rect[1] and
            coords[1] <= rect[1] + rect[3]):
        return True
    else:
        return False

if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode((640, 480))
    ballimg = pygame.image.load("ball.gif")
    ballrect = ballimg.get_rect()
    myfont = pygame.font.SysFont(None, 180)

    direction = 1

    variable_clock_frame_skip = 10
    physics_clock_frame_skip = 9
    clock_count = 0

    # input handling (somewhat boilerplate code):
    while True:
        clock_count += 1
        break_this = False
        if clock_count == variable_clock_frame_skip * physics_clock_frame_skip:
            clock_count = 0

        pygame.time.wait(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    cursor_coors = pygame.mouse.get_pos()
                    if is_within(cursor_coors, ballrect):
                        label = myfont.render("WINNER!", 1, (255, 255, 0))

                        center = (window.get_width()/2,
                                  window.get_height()/2)

                        window.blit(label,
                                    top_left_coord_of_object_where_mid_is(myfont.size("WINNER!"), center))
                        break_this = True
        if break_this:
            break

        if ballrect[0] + ballrect[2] > 640 or ballrect[0] < 0:
            direction *= -1
        ballrect = ballrect.move([direction*5, 0])

        window.fill((0, 0, 0))
        window.blit(ballimg, ballrect)
        pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        pygame.display.flip()
