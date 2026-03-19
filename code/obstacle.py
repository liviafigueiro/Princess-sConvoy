from code.entity import Entity


class Obstacle(Entity):

    def __init__(self, name: str, position: tuple):

        super().__init__(name, position)

        # velocidade do obstáculo
        self.speed = 5

    def move(self):

        # movimento do runner (direita → esquerda)
        self.rect.x -= self.speed

        # remove se sair da tela
        if self.rect.right < 0:
            self.health = 0