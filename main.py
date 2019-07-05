# -*- coding: utf-8 -*-
# author: Nitromelon
# date: 2019.07.05
# version: 0.0.2

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
        # draw background
        screen.fill(BG_COLOR)
        # collect events
        events = pygame.event.get()
        # alive or not
        if not game_state.snake.alive:
            game_state.end_game()
        # apply events
        check_events(events, game_state, game_resource)
        # draw game area
        GameDisplay.draw_game_area(screen, game_state, game_resource)
        # render the screen
        pygame.display.flip()


if __name__ == '__main__':
    main()
