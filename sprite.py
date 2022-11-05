import pygame
import function
from config import *

class sprite(pygame.sprite.Sprite):
    def __init__(self,pos,group,data):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SPRITE_SIZE-5,SPRITE_SIZE-5))
        self.image.fill(SPRITE_FALSE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]*SPRITE_SIZE
        self.rect.y = pos[1]*SPRITE_SIZE

        self.position = pos
        self.type = False
        self.mouseDown = False
        if data[self.position[1]][self.position[0]]:
            self.type = True

        group.add(self)

    def update(self,data,start,mouse):
        self.set_color(data[self.position[1]][self.position[0]])
        if data[self.position[1]][self.position[0]]:
            self.type == True
        else:
            self.type == False
        if not start:
            if not self.mouseDown:
                if mouse[0]>self.rect.x and mouse[0]<self.rect.x+SPRITE_SIZE and mouse[1]>self.rect.y and mouse[1]<self.rect.y+SPRITE_SIZE and mouse[2]:
                    self.type = not self.type
                    self.mouseDown = True
            elif not(mouse[0]>self.rect.x and mouse[0]<self.rect.x+SPRITE_SIZE and mouse[1]>self.rect.y and mouse[1]<self.rect.y+SPRITE_SIZE):
                self.mouseDown = False

        data[self.position[1]][self.position[0]] = self.type

    def set_color(self,data):
        if data:
            self.type = True
        else:
            self.type = False
        if self.type:
            self.image.fill(SPRITE_TRUE_COLOR)
        else:
            self.image.fill(SPRITE_FALSE_COLOR)