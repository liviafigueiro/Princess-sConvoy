
import sys
import pygame
import random
from pygame.font import Font
from pygame import Rect
from pygame import Surface

from code.Const import (
    C_WHEAT, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY,
    SPAWN_TIME, C_GREEN, C_CYAN, EVENT_TIMEOUT,
    TIMEOUT_STEP, TIMEOUT_LEVEL, WIN_WIDTH
)

from code.enemy import Enemy
from code.enemyShot import EnemyShot
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.entityMediator import EntityMediator
from code.player import Player
from code.playerShot import PlayerShot


class Level:

    def __init__(self, window: Surface, name: str, player_score: list[int]):

        self.window = window
        self.name = name
        self.castle_spawned = False
        self.castle_arrived = False

        self.entity_list: list[Entity] = []



        # background
        bg_list = EntityFactory.get_entity(self.name + 'Bg')
        if bg_list:
            self.entity_list.extend(bg_list)

        self.rules_img = pygame.image.load('../asset/regras.png').convert_alpha()
        self.rules_rect = self.rules_img.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))

        # player 1
        self.player = EntityFactory.get_entity('Player1')
        if self.player:
            self.player.score = player_score[0]
            self.entity_list.append(self.player)

        # tempo da fase
        self.timeout = TIMEOUT_LEVEL



        # eventos automáticos
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):

        if self.name == "Level1":
            self.show_rules()
        pygame.mixer.music.load(f'../asset/{self.name}.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

        clock = pygame.time.Clock()

        while True:

            clock.tick(70)


            # desenhar e mover entidades
            for ent in self.entity_list:

                self.window.blit(ent.surf, ent.rect)

                if isinstance(ent, Enemy):
                    ent.move(self.player)
                    shot = ent.shoot()

                    if shot is not None:
                        self.entity_list.append(shot)
                else:
                    ent.move()


                if ent.name == 'Castle':

                    if ent.rect.x <= 350:  # mesma posição onde ele para
                        self.castle_arrived = True


                if isinstance(ent, Player):

                    shot = ent.shoot()

                    if shot is not None:
                        self.entity_list.append(shot)

                # HUD player 1
                if ent.name == 'Player1':
                    self.level_text(
                        18,
                        f'Carruagem - Health: {ent.health} | Score: {ent.score}',
                        C_GREEN,
                        (10, 25)
                    )

            if self.castle_arrived:
                for ent in self.entity_list:
                    if isinstance(ent, Player): ent.rect.x += 1

            # eventos
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # spawn inimigos
                if event.type == EVENT_ENEMY:

                    choice = random.choice(('Enemy1', 'Rock', 'Log'))

                    entity = EntityFactory.get_entity(choice)

                    if entity is not None:
                        self.entity_list.append(entity)

                # controle do tempo
                if event.type == EVENT_TIMEOUT:

                    self.timeout -= TIMEOUT_STEP

                    if self.timeout <= 0 and not self.castle_spawned:
                        castle = EntityFactory.get_entity('Castle')
                        self.entity_list.append(castle)

                        self.castle_spawned = True


                        pygame.time.set_timer(EVENT_ENEMY, 0)  # para inimigos

                        self.timeout = 9999999  # evita acabar o level imediatamente

                        for ent in self.entity_list:

                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score





            # verificar se existe jogador vivo
            found_player = any(isinstance(ent, Player) for ent in self.entity_list)

            if not found_player:
                pygame.mixer.music.stop()
                self.show_lose()
                return False

            # HUD geral
            self.level_text(
                14,
                f'{self.name} - Timeout: {self.timeout/1000:.1f}s',
                C_WHEAT,
                (10, 5)
            )

            self.level_text(
                14,
                f'fps:{clock.get_fps():.0f}',
                C_WHEAT,
                (10, WIN_HEIGHT - 35)
            )

            self.level_text(
                14,
                f'entidades:{len(self.entity_list)}',
                C_WHEAT,
                (10, WIN_HEIGHT - 20)
            )

            pygame.display.flip()

            # colisões
            EntityMediator.verify_collision(self.entity_list)

            # remover mortos
            EntityMediator.verify_health(self.entity_list)
            # remover tiros de inimigos mortos
            self.entity_list = [
                ent for ent in self.entity_list
                if not (
                        isinstance(ent, EnemyShot) and
                        (ent.owner not in self.entity_list)
                )
            ]
            self.entity_list = [
                ent for ent in self.entity_list
                if not (
                        isinstance(ent, PlayerShot) and ent.lifetime <= 0
                )
            ]

            for ent in self.entity_list:
                if isinstance(ent, Player):

                    for other in self.entity_list:

                        if other.name == 'Castle':

                            if ent.rect.colliderect(other.rect):
                                player_score[0] = ent.score
                                pygame.mixer.music.stop()

                                self.show_victory()
                                return True

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):

        text_font: Font = pygame.font.SysFont(
            'Lucida Sans Typewriter',
            text_size
        )

        text_surf: Surface = text_font.render(
            text,
            True,
            text_color
        ).convert_alpha()

        text_rect: Rect = text_surf.get_rect(
            left=text_pos[0],
            top=text_pos[1]
        )

        self.window.blit(text_surf, text_rect)

    def show_rules(self):

        waiting = True

        while waiting:

            self.window.fill((0, 0, 0))

            self.window.blit(self.rules_img, self.rules_rect)

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False

    def show_victory(self):
            waiting = True


            if self.name == 'Level1':
                img = pygame.image.load('../asset/victory.png').convert_alpha()
            else:
                img = pygame.image.load('../asset/win.png').convert_alpha()
                pygame.mixer.music.load('../asset/win.wav')
                pygame.mixer.music.play(0)
            rect = img.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
            while waiting:
                self.window.fill((0, 0, 0))
                self.window.blit(img, rect)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        waiting = False

                pygame.display.flip()
    def show_lose(self):
        waiting = True
        pygame.mixer.music.load('../asset/lose.wav')
        pygame.mixer.music.play(0)
        lose_img = pygame.image.load('../asset/lose.png').convert_alpha()
        lose_rect = lose_img.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))

        while waiting:
            self.window.fill((0, 0, 0))
            self.window.blit(lose_img, lose_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False

            pygame.display.flip()