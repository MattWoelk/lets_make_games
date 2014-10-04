from __future__ import (division,
                        with_statement,
                        print_function,
                        unicode_literals)
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


class BallGame:
    def __init__(self):
        self.window = pygame.display.set_mode((640, 480))
        self.ballimg = pygame.image.load("ball.gif")
        self.ballbounds = self.ballimg.get_rect()
        self.myfont = pygame.font.SysFont(None, 180)
        self.direction = 1
        self.win_state = False

    def update(self, surface, inputs):
        self.update_ball()
        self.redraw(surface)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                cursor_coors = pygame.mouse.get_pos()
                if is_within(cursor_coors, self.ballbounds):
                    self.show_text("WINNER!")
                    self.win_state = True

    def redraw(self, surface):
        self.window.fill((0, 0, 0))
        surface.blit(self.ballimg, self.ballbounds)

    def make_label(self, string):
        return self.myfont.render(string, 1, (255, 255, 0))

    def centre(self):
        return (self.window.get_width()/2,
                self.window.get_height()/2)

    def show_text(self, text):
        label = ballGame.make_label(text)
        self.window.blit(
            label,
            top_left_coord_of_object_where_mid_is(
                self.myfont.size(text),
                self.centre()))

    def update_ball(self):
        if self.ball_at_edge():
            self.reverse_ball()
        self.ballbounds = self.ballbounds.move([self.direction*5, 0])

    def ball_at_edge(self):
        return (self.ballbounds[0] + self.ballbounds[2] > 640 or
                self.ballbounds[0] < 0)

    def reverse_ball(self):
        self.direction *= -1


def quit_if_escape(event):
    if event.type == pygame.QUIT:
        sys.exit(0)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            sys.exit(0)


if __name__ == '__main__':
    pygame.init()

    ballGame = BallGame()

    # input handling (somewhat boilerplate code):
    while True:
        break_this = False

        pygame.time.wait(10)
        events = pygame.event.get()
        for event in events:
            quit_if_escape(event)

        ballGame.update(pygame.display.get_surface(),
                        events)
        if ballGame.win_state:
            break
        pygame.display.flip()

    while True:
        for event in pygame.event.get():
            quit_if_escape(event)
        pygame.display.flip()
