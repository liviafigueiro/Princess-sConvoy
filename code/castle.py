from code.entity import Entity


class Castle(Entity):

    def __init__(self, name, position):
        super().__init__(name, position)

        self.speed = 2

    def move(self):
        # posição onde o castelo deve parar
        stop_position = 350

        if self.rect.x > stop_position:
            self.rect.x -= self.speed