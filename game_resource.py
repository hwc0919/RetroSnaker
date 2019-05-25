import pygame

from settings import *


class GameResource():
    def __init__(self):
        self.load_text()

    def load_text(self):
        welcome_font = pygame.font.Font(None, 40)
        prompt_font = pygame.font.Font(None, 20)
        self.welcome_text = welcome_font.render(
            'Retro Snaker', 1, TEXT_COLOR)
        self.game_over_text = welcome_font.render(
            'Game Over', 1, TEXT_COLOR)
        self.start_prompt = prompt_font.render(
            'Press Enter to start', 1, TEXT_COLOR)

    def load_bg_img(self):
        pass

    def load_bg_music(self):
        pass
