from __future__ import (division,
                        with_statement,
                        print_function,
                        unicode_literals)
import sys
import pygame
import cairo
from math import pi


def top_left_coord_of_object_where_mid_is(text_object_size, mid_coords):
    return (mid_coords[0] - (text_object_size[0]/2),
            mid_coords[1] - (text_object_size[1]/2))


def inner_intersects_outer(inner, outer):
    return (inner[0] + inner[2] > outer[2] or
            inner[0] < outer[0] or
            inner[1] + inner[3] > outer[3] or
            inner[1] < outer[1])


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
        self.ballimg = pygame.image.load("ball.gif")
        self.ballbounds = self.ballimg.get_rect()
        self.myfont = pygame.font.SysFont(None, 180)
        self.direction = 1
        self.win_state = False

    def update(self, surface, events):
        self.update_ball(surface)
        self.redraw(surface)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                cursor_coors = pygame.mouse.get_pos()
                if is_within(cursor_coors, self.ballbounds):
                    self.show_text("WINNER!", surface)
                    self.win_state = True

    def redraw(self, surface):
        surface.fill((0, 0, 0))
        surface.blit(self.ballimg, self.ballbounds)

    def make_label(self, string):
        return self.myfont.render(string, 1, (255, 255, 0))

    def centre(self, surface):
        return (surface.get_width()/2,
                surface.get_height()/2)

    def show_text(self, text, surface):
        label = ballGame.make_label(text)
        surface.blit(
            label,
            top_left_coord_of_object_where_mid_is(
                self.myfont.size(text),
                self.centre(surface)))

    def update_ball(self, surface):
        if inner_intersects_outer(inner=self.ballbounds,
                                  outer=surface.get_rect()):
            self.reverse_ball()
        self.ballbounds = self.ballbounds.move([self.direction*5, 0])

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
    pygame.display.set_mode((640, 480))

    surface = cairo.SVGSurface('test.svg', 600, 400)
    cr = cairo.Context(surface)
    cr.scale(600, 400)
    cr.set_line_width(0.1)
    cr.set_source_rgb(0, 0, 0)
    cr.rectangle(0.25, 0.25, 0.5, 0.5)
    cr.stroke()

    #ballGame = BallGame()

    ## input handling (somewhat boilerplate code):
    while True:
        break_this = False

        pygame.time.wait(10)
        events = pygame.event.get()
        for event in events:
            quit_if_escape(event)

    #    ballGame.update(pygame.display.get_surface(),
    #                    events)
    #    if ballGame.win_state:
    #        break
    #    pygame.display.flip()

    #ballGame = BallGame()

    #while True:
    #    pygame.time.wait(10)
    #    events = pygame.event.get()
    #    for event in events:
    #        quit_if_escape(event)
    #    ballGame.update(pygame.display.get_surface(),
    #                    events)
    #    if ballGame.win_state:
    #        break
    #    pygame.display.flip()

    #pygame.time.wait(2000)

    #while True:
    #    pygame.time.wait(10)
    #    for event in pygame.event.get():
    #        quit_if_escape(event)
    #    pygame.display.flip()
