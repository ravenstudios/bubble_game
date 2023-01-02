from constants import *
import pygame
import random

class Bubble(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x, self.y = x, y
        self.width = GRID_SIZE
        self.height = GRID_SIZE

        self.color = COLORS[random.randint(0, len(COLORS) - 1)]
        self.image = pygame.Surface((GRID_SIZE, GRID_SIZE))
        self.image.fill(self.color)
        self.rect = pygame.Rect(self.image.get_rect())

        self.rect.topleft = (x, y)

        self.drop_speed = 5
        self.is_past_dispenser = False

    def update(self, bubbles):
        if self.rect.top > 0:
            self.is_past_dispenser = True
        if self.rect.bottom < GAME_HEIGHT and self.is_space_below_empty(bubbles):
            self.fall()


        if pygame.mouse.get_pressed() == (1, 0, 0):
            self.clicked()

    def fall(self):
        self.rect = self.rect.move(0, self.drop_speed)

    def is_space_below_empty(self, bubbles):
        for b in bubbles:
            if b != self:
                if b.rect.x == self.rect.x and b.rect.bottom > self.rect.bottom:
                    if self.rect.bottom + self.drop_speed > b.rect.top:
                        self.rect.bottom = b.rect.top
                        return False
        return True

    def clicked(self, bubbles):
        mp = pygame.mouse.get_pos()

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.kill()
