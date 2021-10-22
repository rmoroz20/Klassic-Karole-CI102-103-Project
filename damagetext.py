#Name of File: damagetext.py
#Purpose: Implements text of fight that shows that a hit has been landed and decreased the health of one of the in-game sprites
#Version and Date: Version 1, last updated March 2021
#Author(s): Ashton Foster
#Dependencies: pygame

import pygame

class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, color):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 35) #setting font
        self.image = self.font.render(damage, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0

    def getCounter(self):
        return self.counter

    def update(self):
        # move damage text
        self.rect.y -= 1
        # delete text after time
        self.counter += 1
        if self.counter > 25:
            self.kill()
