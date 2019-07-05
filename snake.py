import numpy as np

from settings import *


class Snake():
    def __init__(self):
        self.length = 5
        self.path = np.array(
            [(10, 10), (11, 10), (12, 10), (13, 10), (14, 10)])
        self.direction = np.array([1, 0])
        self.next_direction = self.direction
        self.alive = True

    # def to_lines(self):
    #     snake_lines = []
    #     i = 0
    #     while i < self.length - 1:
    #         start = self.path[i]
    #         direction = (self.path[i + 1] - self.path[i])
    #         for j in range(i, self.length - 1):
    #             if all(self.path[j] + direction == self.path[j + 1]):
    #                 continue
    #             else:
    #                 end = self.path[j]
    #                 i = j
    #                 break
    #         else:
    #             end = self.path[j + 1]
    #             i = j + 1
    #         snake_lines.append((start, end))
    #     return snake_lines

    # stores turning operation temporarily (only the last directional key pressed will count)
    def to_turn(self, direction):
        self.next_direction = np.array(direction)

    # snake turns direction
    def turn(self):
        if all(self.direction + self.next_direction == [0, 0]):
            pass
        else:
            self.direction = self.next_direction

    # walk one step, return -1 if will hit, 1 if eat the apple, 0 otherwise
    def walk(self, apple):
        self.turn()
        to_walk = self.path[-1] + self.direction
        # 是否会撞墙
        if self.will_hit(to_walk):
            self.alive = False
            return False
        elif all(to_walk == apple):
            self.path = np.r_[self.path, [to_walk]]
            return True
        else:
            self.path = np.r_[self.path, [to_walk]][1:]
            return False

    # snake will hit wall or itself
    def will_hit(self, to_walk):
        return not (0 <= to_walk[0] < BOARD_WIDTH and
                    0 <= to_walk[1] < BOARD_HEIGHT and
                    not any(all(res) for res in to_walk == self.path[:-1]))
