#!/usr/bin/python
from code.entity import Entity
from code.Const import ENTITY_SHOT_DELAY
from code.enemyShot import EnemyShot


class Enemy(Entity):

    def __init__(self, name, position):

        super().__init__(name, position)

        self.speed = 4

        # cooldown do tiro
        self.shot_delay = ENTITY_SHOT_DELAY.get(self.name, 120)

    def move(self, player=None):

        # movimento normal
        self.rect.x -= self.speed

        # se tiver jogador e estiver perto → acelera
        if player:

            distance = self.rect.x - player.rect.x



    def shoot(self):


        self.shot_delay -= 1

        if self.shot_delay <= 0:


            self.shot_delay = ENTITY_SHOT_DELAY.get(self.name, 120)

            return EnemyShot(
                name=f'{self.name}Shot',
                position=(self.rect.left, self.rect.centery)
            )

        return None