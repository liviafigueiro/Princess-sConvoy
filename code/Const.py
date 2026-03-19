#C
import pygame

C_ORANGE = (255, 128, 0)
C_WHEAT= (245, 222, 179)
# C_ORCHID = (218, 112, 214)
C_GOLD = (218, 165, 32)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

#E
EVENT_ENEMY = pygame.USEREVENT +1
EVENT_TIMEOUT = pygame.USEREVENT +2

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Rock': 200,
    'Log': 200,
    'Player1': 1,
    'Player1Shot': 35,
    'Enemy1': 1,
    'Enemy1Shot': 25,
    'Enemy2': 1,
    'Enemy2Shot': 40,
    'Castle': 0

}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Rock': 0,
    'Log': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
    'Castle':0
}


ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Rock': 4,
    'Log': 4,
    'Player1': 3,
    'Player1Shot': 1,
    'Enemy1': 1,
    'Enemy1Shot': 3,
    'Enemy2': 1,
    'Enemy2Shot': 5,
    'Castle': 0.1
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Enemy1':90,
    'Enemy2': 90,

}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Rock': 999,
    'Log': 999,
    'Player1': 200,
    'Player1Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Castle': 999


}


#M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT',)
#P
PLAYER_KEY_UP = {'Player1': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RSHIFT}


#S
SPAWN_TIME = 2000

#T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 20000 #20 segundos

#W
WIN_WIDTH = 576
WIN_HEIGHT = 324

#G
GROUND_Y = WIN_HEIGHT - 10


SCORE_POS = {

    'EnterNameLabel': (250, 150),
    'EnterNameInput': (250, 190),
    'NameLabel': (250, 120),
    'ScoreLabel': (450, 120),
    'DateLabel': (550, 120),

    0: (250, 160),
    1: (250, 190),
    2: (250, 220),
    3: (250, 250),
    4: (250, 280),
    5: (250, 310),
    6: (250, 340),
    7: (250, 370),
    8: (250, 400),
    9: (250, 430),
}