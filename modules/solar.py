import pygame
import sys


def Solar(Window):
    while True:
        Window.fill("black")

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
