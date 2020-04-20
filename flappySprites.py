import pygame
from flappySetting import *

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = new_bird.convert_alpha()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)
        self.vel = vec(0, 0)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.acc = vec(0, 0)

    def jump(self):
        self.vel.y = -PLAYER_JUMP

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)

        # friction
        self.acc.x += self.vel.x * PLAYER_FRICTION

        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.y < 0:
            self.pos.y = HEIGHT
        elif self.pos.y > HEIGHT:
            self.pos.y = HEIGHT
        self.rect.midbottom = self.pos


class Obs(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.all_sprites, game.obs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((w, h))
        self.image.fill(random.choice(OBS_COLOUR))
        self.rect = self.image.get_rect()
        self.last_update = 0
        self.rect.x = x
        self.rect.y = y

