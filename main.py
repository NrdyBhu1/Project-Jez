import pygame
from pygame.locals import * 
import sys
from utils import *
from window import Window

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()

game_running = True

display = pygame.display.set_mode((512, 512))
pygame.display.set_caption('Project Jaz')

roboto = pygame.font.Font('./assets/fonts/Roboto-Regular.ttf', 25)

pygame.mouse.set_visible(False)

main_window = Window((512, 512), (50, 50, 150))

new_win = Window((424, 200), (150, 150, 50), font=roboto, title="Quit?", active=True)

while game_running:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            game_running = False 
        if ev.type == KEYDOWN:
            if ev.key == K_ESCAPE:
                game_running = False

        main_window.update(ev)
        new_win.update(ev)

    display.fill((0, 0, 0))
    display.blit(main_window.surface, (0, 0))
    display.blit(new_win.surface, (50, 150))
    pygame.display.flip()
    clock.tick(40)

pygame.mouse.set_visible(True)

pygame.quit()
sys.exit()
