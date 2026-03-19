#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu
from code.score import Score




class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            # NEW GAME
            if menu_return == MENU_OPTION[0]:
                player_score = [0]

                level = Level(self.window, 'Level1', player_score)
                level_return = level.run(player_score)

                if level_return:
                    level = Level(self.window, 'Level2', player_score)
                    level_return = level.run(player_score)

                    if level_return:
                        score.save(player_score)

            # SCORE
            elif menu_return == MENU_OPTION[1]:
                score.show()

            # EXIT
            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                sys.exit()

