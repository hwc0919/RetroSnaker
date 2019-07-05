import random

import pygame

from settings import *
from snake import Snake


class GameState():
    def __init__(self, screen):
        self.screen = screen
        self.round = 0
        self.snake = Snake()
        self.apple = None
        self.apple_eaten = True
        self.interval = SNAKE_SPEED
        self.game_timer = None
        self.active = False

    # set a timer that triggers USEREVENT every interval time
    def set_timer(self, interval):
        self.game_timer = pygame.time.set_timer(pygame.USEREVENT, interval)

    # generate an apple
    def gen_apple(self):
        i = random.randrange(BOARD_WIDTH)
        j = random.randrange(BOARD_HEIGHT)
        while any(all(res) for res in (i, j) == self.snake.path):
            i = random.randrange(BOARD_WIDTH)
            j = random.randrange(BOARD_HEIGHT)
        self.apple = (i, j)
        self.apple_eaten = False

    # reset everything and start game
    def start_game(self):
        self.round += 1
        self.snake.__init__()
        self.apple = None
        self.apple_eaten = True
        self.interval = SNAKE_SPEED
        self.game_timer = self.set_timer(self.interval)
        self.active = True

    # stop the timer and end the game
    def end_game(self):
        self.active = False
        self.set_timer(0)
