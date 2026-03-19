import pygame

from code.Const import (
    ENTITY_SPEED, WIN_WIDTH,
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT,
    ENTITY_SHOT_DELAY, GROUND_Y
)

from code.entity import Entity
from code.playerShot import PlayerShot


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

        # SOM DA MAGIA
        self.shoot_sound = pygame.mixer.Sound('../asset/magic.wav')
        self.shoot_sound.set_volume(0.3)

        # física do pulo
        self.vel_y = 0
        self.gravity = 0.3
        self.jump_force = -12
        self.on_ground = True

    def move(self):

        pressed_key = pygame.key.get_pressed()

        # pulo
        if pressed_key[pygame.K_SPACE] and self.on_ground:
            self.vel_y = self.jump_force
            self.on_ground = False

        # aplicar gravidade
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        # colisão com o chão
        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.vel_y = 0
            self.on_ground = True

    def shoot(self):
            pressed_key = pygame.key.get_pressed()

            if pressed_key[PLAYER_KEY_SHOOT[self.name]] and self.shot_delay <= 0:
                self.shot_delay = ENTITY_SHOT_DELAY[self.name]

                self.shoot_sound.play()

                return PlayerShot(
                    name=f'{self.name}Shot',
                    position=(self.rect.right, self.rect.centery)
                )

            self.shot_delay -= 1

            return None



