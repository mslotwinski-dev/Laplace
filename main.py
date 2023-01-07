import pygame
import sys

from modules.menu import Menu
from modules.solar import Solar

pygame.init()

WIDTH, HEIGHT = 1200, 800

Window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tesla")


clock = pygame.time.Clock()
clock.tick(144)


def main():
    Menu(Window)


main()
