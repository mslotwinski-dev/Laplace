import pygame
import sys

from helpers.font import get_font
from modules.solar import Solar

from components.button import Button

LogoImage = pygame.image.load("assets/img/Logo.png")
LogoImage = pygame.transform.scale(LogoImage, (700, 100))


def Menu(Window):
    while True:
        Window.fill("#E3E3E3")

        MOUSE_POS = pygame.mouse.get_pos()

        LOGO_RECT = LogoImage.get_rect(center=(600, 90))
        Window.blit(LogoImage, LOGO_RECT)

        SELECT_TEXT = get_font(
            "Rubik-Medium", 35).render("SELECT SIMULATION", True, "#00647d")
        SELECT_RECT = SELECT_TEXT.get_rect(topleft=(30, 180))
        Window.blit(SELECT_TEXT, SELECT_RECT)

        # BUTTONS
        SOLAR_SYSTEM = Button(image=pygame.image.load("assets/img/button.png"), pos=(185, 280),
                              text_input="SOLAR SYSTEM", font=get_font("Rubik-Medium", 25), base_color="#e3e3e3", hovering_color="#e3e3e3")

        for button in [SOLAR_SYSTEM]:
            button.changeColor(MOUSE_POS)
            button.update(Window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SOLAR_SYSTEM.checkForInput(MOUSE_POS):
                    Solar(Window)

        pygame.display.update()
