"""
Author: Shivang
Created on: 28/3/20
Purpose:  Flappy bird
"""

import pygame
import random

from flappySetting import *

from flappySprites import *


class Game:

    def __init__(self):

        # initialize game window, etc

        pygame.init()

        pygame.mixer.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)

        self.clock = pygame.time.Clock()

        self.running = True
        # bg_music = pygame.mixer.music.load('flappy_assests/Tavern.ogg')
        self.data_load()

    def data_load(self):
        with open("score.txt", "r+") as file:
            try:
                self.highscore = int(file.readline())
            except:
                self.highscore = 0

    def new(self):

        # start a new game
        self.score = 0
        self.all_sprites = pygame.sprite.Group()
        self.obs = pygame.sprite.Group()
        # self.obs_down = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        for plat in OBS_LIST:
            Obs(self, *plat)
        self.run()

    def run(self):

        # Game Loop

        self.playing = True

        while self.playing:
            self.clock.tick(FPS)

            self.events()

            self.update()

            self.draw()

    def update(self):
        # sound =pygame.mixer.Sound('coin.mp3')
        # Game Loop - Update
        self.all_sprites.update()
        if self.player.pos.x >= 0:
            # self.player.pos.y += max(abs(self.player.vel.y), 3)
            for plat in self.obs:
                plat.rect.x -= max(abs(self.player.vel.x), 3.5)

                if plat.rect.left < 0:
                    self.score += 5
                    sound = pygame.mixer.Sound('flappy_assests/sfx_point.wav')
                    sound.play()
                    plat.kill()
        while len(self.obs) < 4:
            height = random.randrange(100, 200)  # x,y,w,h
            Obs(self, WIDTH / 2 + 200, 0, 50, height)
            point = random.randrange(400, 0, -105)
            Obs(self, WIDTH / 2 + 200, point + 200, 50, 1000)
        hits = pygame.sprite.spritecollide(self.player, self.obs, False, False)
        if hits:
            sound = pygame.mixer.Sound('flappy_assests/sfx_hit.wav')
            sound.play()
            self.playing = False

    def events(self):
        # Game Loop - events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font('flappy_assests/BRLNSR.ttf', size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw(self):
        # Game Loop - draw
        self.screen.blit(back_im, (0, 0))

        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 35, BLACK, WIDTH / 2, 50)

        # *after* drawing everything, flip the display

        pygame.display.flip()

    def show_start_screen(self):

        # game splash/start screen
        self.screen.fill(WHITE)
        self.screen.blit(start_bg, (0, 0))
        self.draw_text(TITLE, 65, BLACK, WIDTH / 2, HEIGHT / 4)
        self.draw_text("BY SHIVANG", 26, (102, 0, 102), WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press TAB to continue...", 20, BLACK, WIDTH / 2, HEIGHT - 100)
        self.draw_text("HIGH SCORE " + str(self.highscore), 15, BLACK, WIDTH / 2, HEIGHT - 20)
        pygame.display.flip()
        self.wait_for_key()

    def show_go_screen(self):

        # game over/continue
        if self.running == False:
            return  # ends this function
        self.screen.fill(Teal)  # ((153, 55, 153))
        self.draw_text("GAME OVER!", 65, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score : " + str(self.score), 25, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press TAB to restart...", 20, WHITE, WIDTH / 2, HEIGHT - 100)
        self.draw_text("HIGH SCORE " + str(self.highscore), 15, BLACK, WIDTH / 2, HEIGHT - 20)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("NEW HIGH SCORE", 20, WHITE, WIDTH / 2, HEIGHT - 150)
            with open("score.txt", "w") as file:
                file.write(str(self.highscore))
        else:
            self.draw_text("HIGH SCORE " + str(self.highscore), 15, WHITE, WIDTH / 2, HEIGHT - 20)
        pygame.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        waiting = False


g = Game()

g.show_start_screen()
# pygame.mixer.music.play(-1)

while g.running:
    g.new()
    g.show_go_screen()
pygame.quit()
