import pygame
import random

WIDTH = 480
HEIGHT = 600
FPS = 120
TITLE = 'Flappy2.0'
ICON = pygame.image.load('flappy_assests//newwgl.png')
# colours
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
SKYBLUE = (0, 155, 155)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
Teal = (0, 128, 128)
Silver = (192, 192, 192)
Fuchsia = (255, 0, 255)
Olive = (128, 128, 0)
Aqua = (0, 255, 255)

# player
PLAYER_GRAV = 0.6
PLAYER_ACC = 0.2
PLAYER_FRICTION = -0.12
PLAYER_JUMP = 11

OBS_LIST = [(WIDTH / 2, 0, 50, 100),
            (WIDTH / 2 + 100, 0, 50, 200),
            (WIDTH / 2 + 203, 0, 50, 200),
            (WIDTH / 2 + 350, 0, 50, 200)
            ]

# bird im
bird_im_list = ['flappy_assests/birdy.png', 'flappy_assests/whity.png']
bird_im = pygame.image.load(random.choice(bird_im_list))
new_bird = pygame.transform.scale(bird_im, (70, 65))

# background
back_im_list = ['flappy_assests/bgbuild.jpg', 'flappy_assests/bgfl.jpg', 'flappy_assests/bgbl.jpg',
                'flappy_assests/bgfr.jpg']
back = pygame.image.load(random.choice(back_im_list))
back_im = pygame.transform.scale(back, (WIDTH, HEIGHT))

# obs colour
OBS_COLOUR = [(102, 0, 102), (102, 255, 102), (155, 55, 0), GREEN, (153, 0, 153), SKYBLUE, Teal, Aqua, Fuchsia, Silver]
start_bg = pygame.image.load('flappy_assests/startbg.png')
# stat=pygame.transform.scale(start_bg,(WIDTH,HEIGHT))
