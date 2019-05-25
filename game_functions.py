import sys

import pygame


def check_events(events, game_state, game_resource):
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if not game_state.active and\
                    event.key == pygame.K_RETURN:
                game_state.start_game()
            elif event.key == pygame.K_UP:
                game_state.snake.to_turn((0, -1))
            elif event.key == pygame.K_DOWN:
                game_state.snake.to_turn((0, 1))
            elif event.key == pygame.K_LEFT:
                game_state.snake.to_turn((-1, 0))
            elif event.key == pygame.K_RIGHT:
                game_state.snake.to_turn((1, 0))
        elif event.type == pygame.USEREVENT:
            game_state.apple_eaten = game_state.snake.walk(game_state.apple)
            game_state.active = game_state.snake.alive
