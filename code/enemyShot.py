from code.Const import ENTITY_SPEED
from code.entity import Entity


class EnemyShot(Entity):

    def __init__(self, name: str, position: tuple, owner):
        super().__init__(name, position)
        self.owner = owner

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]