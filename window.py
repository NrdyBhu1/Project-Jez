#!/usr/bin/env python3

import pygame
from utils import *

class Window:
    def __init__(self, size, color, font=None, title=None, disabled=False, active=False):
        self.size = size
        self.color = color
        self.active = active
        self.title = None
        if title:
            self.title = font.render(title, False, (255, 255, 255))
            self.shadow = font.render(title, False, (0, 0, 0))
        self.surface = pygame.Surface(size)
        self.disabled = disabled



    def toggle_active(self):
        self.active = not self.active

    def toggle_disable(self):
        self.disabled = not self.disabled

    def update(self, event):

        self.surface.fill(darken_color(self.color, 50))

        if not self.disabled:
            if self.active:
                self.surface.fill(brighten_color(self.color, 50))
                pygame.draw.line(self.surface, (100, 100, 100), (1, 1), (1, self.size[1]-3), 2)
                pygame.draw.line(self.surface, (100, 100, 100), (1, self.size[1]-3), (self.size[0]-3, self.size[1]-3), 2)
                pygame.draw.line(self.surface, (100, 100, 100), (self.size[0]-3, self.size[1]-3), (self.size[0]-3, 1), 2)
                pygame.draw.line(self.surface, (100, 100, 100), (self.size[0]-3, 1), (1, 1), 2)
            else:
                self.surface.fill(self.color)

        if self.title:
            self.surface.blit(self.shadow, (self.size[0]/2 - self.title.get_width()/2 + 2, 2))
            self.surface.blit(self.title, (self.size[0]/2 - self.title.get_width()/2, 0))
