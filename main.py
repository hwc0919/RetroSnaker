# -*- coding: utf-8 -*-
# author: Nitromelon on fire
# date: 2019.05.25
# version: 0.0.1

import pygame

from game_display import GameDisplay
from game_functions import check_events
from game_resource import GameResource
from game_state import GameState
from settings import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Retro Snaker')
    game_resource = GameResource()
    game_state = GameState(screen)

    while True:
        screen.fill(BG_COLOR)
        events = pygame.event.get()
        if not game_state.snake.alive:
            game_state.end_game()
        check_events(events, game_state, game_resource)
        GameDisplay.draw_game_area(screen, game_state, game_resource)
        pygame.display.flip()


if __name__ == '__main__':
    main()
