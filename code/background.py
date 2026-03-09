#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.entity import Entity


class Background(Entity):
    def __init__(self, name:str, position:tuple):
        super().__init__(name, position)
        pass

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name] #velocidade
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH #quando a imagem chega ao final da tela,
            # ela retorna ao início

