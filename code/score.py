import datetime
import sys

import pygame
from pygame import Rect, KEYDOWN
from pygame.constants import K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font
from pygame.surface import Surface

from code.Const import C_GOLD, SCORE_POS, MENU_OPTION, C_WHEAT
from code.DBProxy import DBProxy


class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('../asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, player_score: list[int]):
        pygame.mixer.music.load('../asset/score.wav')
        pygame.mixer.music.play(-1)

        db_proxy = DBProxy('DBScore')
        name = ''
        score = int(player_score[0])

        while True:
            self.window.blit(self.surf, self.rect)

            self.text(28, 'Enter your name (4 characters):', C_WHEAT, SCORE_POS['EnterNameLabel'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({
                            'name': name,
                            'score': score,
                            'date': get_formatted_date()
                        })
                        db_proxy.close()
                        self.show()
                        return

                    elif event.key == K_BACKSPACE:
                        name = name[:-1]

                    else:
                        if len(name) < 4 and event.unicode.isprintable():
                            name += event.unicode

            self.text(40, name, C_WHEAT, SCORE_POS['EnterNameInput'])
            pygame.display.flip()

    def show(self):
            pygame.mixer.music.load('../asset/score.wav')
            pygame.mixer.music.play(-1)

            self.window.blit(self.surf, self.rect)

            db_proxy = DBProxy('DBScore')
            list_score = db_proxy.retrieve_top10()
            db_proxy.close()

            # TÍTULOS DAS COLUNAS
            self.text(28, 'NAME', C_GOLD, (125, 120))
            self.text(28, 'SCORE', C_GOLD, (275, 120))
            self.text(28, 'DATE', C_GOLD, (425, 120))

            # se não tiver score
            if not list_score:
                self.text(24, 'NO SCORES YET', C_WHEAT, (250, 200))
            else:
                for i, player_score in enumerate(list_score):
                    id_, name, score, date = player_score

                    y = 144 + i * 17

                    # Nome
                    self.text(17, name, C_WHEAT, (125, y))

                    # Score
                    self.text(17, f'{int(score):05d}', C_WHEAT, (275, y))
                    # Data
                    self.text(17, date, C_WHEAT, (425, y))

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            return

                pygame.display.flip()

    def text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont('Franklin Gothic Medium', text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)

def get_formatted_date():
    current_datetime = datetime.datetime.now()
    current_time = current_datetime.strftime('%H:%M')
    current_date = current_datetime.strftime('%d-%m-%Y')
    return f"{current_time} - {current_date}"