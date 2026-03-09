#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha() #carregar imagem
        self.rect = self.surf.get_rect(left=0, top=0) #criar retangulo



    def run(self):
        menu_option = 0
        pygame.mixer.music.load('./asset/Menu.mp3')  # carregar a musica
        pygame.mixer.music.play(-1)  # fazer a música tocar, -1 deixa ela tocando infinita
        pygame.mixer.music.set_volume(0.3)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # colocar imagem no retangulo
            self.menu_text(65,"Mountain", C_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(65, "Shooter", C_ORANGE, ((WIN_WIDTH / 2), 110))

            for i in range(len(MENU_OPTION)):

                if i == menu_option:
                    self.menu_text(25, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(25, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))
                #vai percorrer cada frase da lista e a cada posição somar 30 * o num da posição


            pygame.display.flip() #atualizar imagem na tela

            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #close window
                    quit() #end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: #DOWN KEY
                        if menu_option <len(MENU_OPTION) - 1:
                            menu_option +=1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP: #UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: #ENTER
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text:str, text_color:tuple, text_center_pos:tuple):
        text_font: Font = pygame.font.SysFont('Lucinda Sans Typewriter', text_size) #diz qual fonte utilizar
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()#faz a fonte virar uma imagem
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)#criar um retangulo para a imagem
        self.window.blit(source=text_surf, dest=text_rect)#atualizar