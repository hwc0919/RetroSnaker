import pygame

from settings import *


class GameDisplay():
    @staticmethod
    def draw_boarder(screen):
        pygame.draw.line(screen, BORDER_COLOR, BOARD_LEFT_TOP,
                         BOARD_RIGHT_TOP, BORDER_WIDTH)
        pygame.draw.line(screen, BORDER_COLOR, BOARD_LEFT_BOTTOM,
                         BOARD_RIGHT_BOTTOM, BORDER_WIDTH)
        pygame.draw.line(screen, BORDER_COLOR, BOARD_LEFT_TOP,
                         BOARD_LEFT_BOTTOM, BORDER_WIDTH)
        pygame.draw.line(screen, BORDER_COLOR, BOARD_RIGHT_TOP,
                         BOARD_RIGHT_BOTTOM, BORDER_WIDTH)

    @staticmethod
    def draw_cell(screen, color, pos):
        pos = (BOARD_LEFT + pos[0] * CELL_WIDTH,
               BOARD_TOP + pos[1] * CELL_WIDTH)
        pygame.draw.rect(screen, color, (pos, (CELL_WIDTH, CELL_WIDTH)))

    @staticmethod
    def draw_snake(screen, snake, color=SNAKE_COLOR):
        for pos in snake.path:
            GameDisplay.draw_cell(screen, color, pos)
        GameDisplay.draw_apple(screen, snake.path[-1],
                               color=SNAKE_HEAD_COLOR, radius=SNAKE_HEAD_RADIUS)

    @staticmethod
    def draw_apple(screen, apple, color=APPLE_COLOR, radius=APPLE_RADIUS, width=0):
        pos = (BOARD_LEFT + apple[0] * CELL_WIDTH + CELL_WIDTH // 2,
               BOARD_TOP + apple[1] * CELL_WIDTH + CELL_WIDTH // 2)
        pygame.draw.circle(screen, color, pos, radius, width)

    @staticmethod
    def draw_game_area(screen, game_state, game_resource):
        GameDisplay.draw_boarder(screen)
        if game_state.active:
            GameDisplay.draw_snake(screen, game_state.snake)
            if game_state.apple_eaten:
                game_state.gen_apple()
            GameDisplay.draw_apple(screen, game_state.apple)
        elif game_state.round == 0:
            screen.blit(game_resource.welcome_text,
                        (BOARD_CENTER - 80, BOARD_MIDDLE - 50))
            screen.blit(game_resource.start_prompt,
                        (BOARD_CENTER - 55, BOARD_MIDDLE))
        else:
            GameDisplay.draw_snake(screen, game_state.snake)
            GameDisplay.draw_apple(screen, game_state.apple)
            screen.blit(game_resource.game_over_text,
                        (BOARD_CENTER - 65, BOARD_MIDDLE - 50))
            screen.blit(game_resource.start_prompt,
                        (BOARD_CENTER - 55, BOARD_MIDDLE))
