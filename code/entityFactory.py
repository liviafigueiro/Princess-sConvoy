#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Const import WIN_WIDTH, WIN_HEIGHT, GROUND_Y
from code.background import Background
from code.enemy import Enemy
from code.obstacle import Obstacle
from code.player import Player
from code.castle import Castle

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(5): #numero de img do level1
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Level2Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Player1':
                player = Player('Player1', (50, 0))
                player.rect.bottom = GROUND_Y
                return player

            case 'Player2':
                player = Player('Player2', (50, 0))
                player.rect.bottom = GROUND_Y
                return player

            case 'Enemy1':
                enemy = Enemy('Enemy1',(WIN_WIDTH+10, 0))
                enemy.rect.bottom = GROUND_Y
                return enemy
            case 'Rock':
                 rock = Obstacle('Rock', (WIN_WIDTH + 10, 0))
                 rock.rect.bottom = GROUND_Y
                 return rock

            case 'Log':
                log = Obstacle('Log', (WIN_WIDTH + 10, 0))
                log.rect.bottom = GROUND_Y
                return log
            case 'Castle':
                castle = Castle('Castle', (WIN_WIDTH + 10, 0))
                castle.rect.bottom = GROUND_Y
                return castle